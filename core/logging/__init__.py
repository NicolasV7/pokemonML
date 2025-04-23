import logging
from typing import Optional
from flask import Flask # type: ignore
from rich.console import Console # type: ignore
from rich.traceback import install # type: ignore
from rich.logging import RichHandler # type: ignore

def configure_logging(app_name: str = "Pokémon Cluster Analyzer", level: int = logging.INFO):
    """
    Configura el sistema de logging centralizado para la aplicación.
    """
    install(show_locals=True, suppress=[Flask])

    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(
            console=Console(),
            show_time=True,
            show_level=True,
            show_path=True,
            markup=True,
        )]
    )

    service_logger = logging.getLogger('services')
    service_logger.setLevel(logging.DEBUG)

    return logging.getLogger(app_name)

def configure_flask_logging(app):
    """
    Configura logging específico para Flask.
    """
    from .handlers import FlaskRichHandler
    from .middlewares import register_logging_middlewares

    app.logger.handlers.clear()
    app.logger.addHandler(FlaskRichHandler())
    app.logger.setLevel(logging.INFO)

    register_logging_middlewares(app)

    logging.getLogger('werkzeug').setLevel(logging.WARNING)

    return app