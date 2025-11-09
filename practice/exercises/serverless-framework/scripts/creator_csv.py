import argparse
import csv
import os
import random
import uuid
from datetime import datetime, timedelta

CATEGORIES = ["A", "B", "C", "D"]


def random_timestamp(start: datetime, end: datetime):
    delta = end - start
    seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=seconds)


def generate_one_csv(path, rows=100):
    start = datetime.now() - timedelta(days=30)
    end = datetime.now()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["id", "timestamp", "value", "category"])
        for _ in range(rows):
            _id = str(uuid.uuid4())
            ts = random_timestamp(start, end).isoformat()
            value = round(random.uniform(0, 1000), 2)
            category = random.choice(CATEGORIES)
            writer.writerow([_id, ts, value, category])


def main():
    parser = argparse.ArgumentParser(description="Genera CSVs fakes")
    parser.add_argument(
        "--count", type=int, default=3, help="Cantidad de archivos a generar"
    )
    parser.add_argument("--rows", type=int, default=200, help="Filas por archivo")
    parser.add_argument(
        "--outdir", type=str, default="./data", help="Directorio de salida"
    )
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    for i in range(args.count):
        filename = f"fake_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i + 1}.csv"
        path = os.path.join(args.outdir, filename)
        generate_one_csv(path, rows=args.rows)
        print(f"Generado: {path}")


if __name__ == "__main__":
    main()
