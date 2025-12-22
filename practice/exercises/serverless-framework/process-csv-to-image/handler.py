import os
import re

import boto3
import matplotlib
import pandas as pd

matplotlib.use("Agg")
import urllib.parse
from datetime import datetime

import matplotlib.pyplot as plt

s3 = boto3.client("s3")
TMP_DIR = "/tmp"
OUTPUT_PREFIX = os.getenv("OUTPUT_PREFIX", "graphs/").strip("/")
if not OUTPUT_PREFIX:
    OUTPUT_PREFIX = "graphs"


def download_s3_object(bucket, key, local_path):
    s3.download_file(bucket, key, local_path)


def upload_s3_bytes(bucket, key, bytes_data, content_type="image/png"):
    s3.put_object(Bucket=bucket, Key=key, Body=bytes_data, ContentType=content_type)


def _sanitize_basename(name: str) -> str:
    """
    Quita extensión, normaliza y deja sólo [a-zA-Z0-9-_].
    """
    base, _ext = os.path.splitext(name)
    base = base.strip()
    base = re.sub(r"[^\w\-]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    return base or "file"


def generate_plot_from_df(df, out_path):
    if "timestamp" in df.columns:
        try:
            df["timestamp_parsed"] = pd.to_datetime(df["timestamp"])
            df_sorted = df.sort_values("timestamp_parsed")
            x = df_sorted["timestamp_parsed"]
            y = pd.to_numeric(df_sorted.get("value", []), errors="coerce")
        except Exception:
            x = range(len(df))
            y = pd.to_numeric(df.get("value", []), errors="coerce")
    else:
        x = range(len(df))
        y = pd.to_numeric(df.get("value", []), errors="coerce")

    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(x, y)
    ax1.set_title("Value over time")
    ax1.set_ylabel("value")
    try:
        fig.autofmt_xdate(rotation=25)
    except Exception:
        pass

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.hist(pd.Series(y).dropna(), bins=30)
    ax2.set_title("Value distribution (histogram)")
    ax2.set_xlabel("value")
    ax2.set_ylabel("frequency")

    plt.tight_layout()
    fig.savefig(out_path, format="png")
    plt.close(fig)


def hello(event, context):
    print("Event:", event)

    for record in event.get("Records", []):
        s3_info = record.get("s3", {})
        bucket = s3_info.get("bucket", {}).get("name")
        raw_key = s3_info.get("object", {}).get("key")
        if not bucket or not raw_key:
            print("No bucket/key en record, salto")
            continue

        key = urllib.parse.unquote_plus(raw_key)
        print(f"Procesando s3://{bucket}/{key}")

        if not key.lower().endswith(".csv"):
            print(f"{key} no es .csv, salto")
            continue

        csv_basename = os.path.basename(key)
        safe_base = _sanitize_basename(csv_basename)

        local_csv = os.path.join(TMP_DIR, csv_basename)
        try:
            download_s3_object(bucket, key, local_csv)
            print(f"Descargado a {local_csv}")

            df = pd.read_csv(local_csv)
            print(f"CSV leído, filas: {len(df)}, columnas: {list(df.columns)}")

            ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
            out_filename = f"{safe_base}-graph-{ts}.png"
            local_png = os.path.join(TMP_DIR, out_filename)

            generate_plot_from_df(df, local_png)
            print(f"Gráfica generada en {local_png}")

            with open(local_png, "rb") as f:
                img_bytes = f.read()

            dest_key = f"{OUTPUT_PREFIX}/{out_filename}"
            upload_s3_bytes(bucket, dest_key, img_bytes)
            print(f"Subido: s3://{bucket}/{dest_key}")

            try:
                os.remove(local_csv)
                os.remove(local_png)
            except Exception:
                pass

        except Exception as e:
            print(f"Error procesando {key}: {e}")

    return {"status": "done"}
