import decimal


def cors_headers() -> dict[str, str]:
    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST",
        "Content-Type": "application/json",
    }


def json_default(o: decimal.Decimal | str) -> float | str | dict:
    if isinstance(o, decimal.Decimal):
        return float(o)
    try:
        import dataclasses

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
    except Exception:
        pass
    return str(o)
