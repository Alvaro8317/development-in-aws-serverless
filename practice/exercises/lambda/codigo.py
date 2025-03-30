from typing import Any


def handler(event: dict[str, Any], context: Any):
    print("Evento es: ", event)
    with open("index.html") as archivo_html:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": archivo_html.read(),
        }
