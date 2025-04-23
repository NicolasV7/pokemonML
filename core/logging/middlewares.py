from flask import request # type: ignore
from rich.text import Text # type: ignore
from rich.panel import Panel # type: ignore

def register_logging_middlewares(app):
    app._got_first_request = False

    @app.before_request
    def log_request_start():
        """Log al inicio de cada petición"""
        if not app._got_first_request:
            _log_startup(app)
            app._got_first_request = True

        if request.path.startswith('/static/'):
            return

        console = Console() # type: ignore
        console.print(
            Panel.fit(
                Text("🌐 Nueva petición", style="bold") + Text("\n") +
                Text("Método: ", style="bold") + Text(request.method, style="request") + Text("\n") +
                Text("Ruta: ", style="bold") + Text(request.path, style="request") + Text("\n") +
                Text("IP: ", style="bold") + Text(request.remote_addr, style="info"),
                border_style="blue"
            )
        )

    @app.after_request
    def log_request_end(response):
        if request.path.startswith('/static/'):
            return response

        status_style = "red" if response.status_code >= 400 else "green"

        console = Console() # type: ignore
        console.print(
            Panel.fit(
                Text("📡 Respuesta", style="bold") + Text("\n") +
                Text("Ruta: ", style="bold") + Text(request.path, style="blue") + Text("\n") +
                Text("Estado: ", style="bold") + Text(str(response.status_code), style=status_style) + Text("\n") +
                Text("Tamaño: ", style="bold") + Text(f"{response.content_length or 0} bytes", style="info"),
                border_style=status_style
            )
        )
        return response

def _log_startup(app):
    console = Console() # type: ignore
    console.print(
        Panel.fit(
            Text("✅ Aplicación lista", style="bold green") + Text("\n") +
            Text("Entorno: ", style="bold") + Text(app.env, style="info") + Text("\n") +
            Text("Debug: ", style="bold") + Text(str(app.debug), style="info") + Text("\n") +
            Text("URL: ", style="bold") + Text("http://127.0.0.1:5000", style="info"),
            title=Text("🚀 Inicio completado", style="bold"),
            border_style="green",
            padding=(1, 4)
        )
    )