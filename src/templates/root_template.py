def get_root_html() -> str:
    return """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Página de Bienvenida</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #4CAF50;
                }
                p {
                    font-size: 1.2em;
                }
                footer {
                    margin-top: 50px;
                    font-size: 0.8em;
                    color: #888;
                }
                .author {
                    font-weight: bold;
                    color: #2c3e50;
                }
            </style>
        </head>
        <body>
            <h1>¡Bienvenido a mi página!</h1>
            <p>Este es un mensaje de prueba, creado con FastAPI.</p>
            <footer>
                <p>Autor: <span class="author">alvaro8317</span></p>
            </footer>
        </body>
        </html>
    """