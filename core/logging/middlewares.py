import logging
from flask import request # type: ignore
from rich.panel import Panel # type: ignore

def register_logging_middlewares(app):
    app._got_first_request = False

    @app.before_request
    def log_request_start():
        if not app._got_first_request:
            logger = logging.getLogger(app.name)
            logger.info(
                Panel.fit(
                    f"[bold green]✅ Aplicación lista[/]\n"
                    f"[bold]Entorno:[/] [info]{app.env}[/]\n"
                    f"[bold]Debug:[/] [info]{app.debug}[/]\n"
                    f"[bold]URL:[/] [info]http://127.0.0.1:5000[/]",
                    title="[bold]🚀 Inicio completado[/]",
                    border_style="green"
                )
            )
            app._got_first_request = True

        logger = logging.getLogger(app.name)
        if request.path.startswith('/static/'):
            return

        logger.info(
            Panel.fit(
                f"[bold]🌐 Nueva petición[/]\n"
                f"[bold]Método:[/] [request]{request.method}[/]\n"
                f"[bold]Ruta:[/] [request]{request.path}[/]\n"
                f"[bold]IP:[/] [info]{request.remote_addr}[/]",
                border_style="request"
            )
        )

    @app.after_request
    def log_request_end(response):
        logger = logging.getLogger(app.name)
        if request.path.startswith('/static/'):
            return response

        status_style = "error" if response.status_code >= 400 else "response"

        logger.info(
            Panel.fit(
                f"[bold]📡 Respuesta[/]\n"
                f"[bold]Ruta:[/] [request]{request.path}[/]\n"
                f"[bold]Estado:[/] [{status_style}]{response.status_code}[/]\n"
                f"[bold]Tamaño:[/] [info]{response.content_length or 0} bytes[/]",
                border_style=status_style
            )
        )
        return response