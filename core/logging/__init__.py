import logging
from rich.console import Console # type: ignore
from rich.traceback import install # type: ignore
from rich.logging import RichHandler # type: ignore

class RichPanelHandler(RichHandler):
    def emit(self, record: logging.LogRecord) -> None:
        if hasattr(record.msg, '__rich__') or isinstance(record.msg, str):
            super().emit(record)
        else:
            console = Console()
            console.print(record.msg)
            record.msg = ""

def configure_logging(app_name: str = "Pokémon Cluster Analyzer"):
    """Configura el sistema de logging centralizado"""
    install(show_locals=True)

    logging.basicConfig(level=logging.INFO, handlers=[])

    root_logger = logging.getLogger()
    root_logger.addHandler(RichPanelHandler(
        console=Console(),
        show_time=True,
        show_level=True,
        show_path=False,
        markup=True,
    ))

    return logging.getLogger(app_name)

def configure_flask_logging(app):
    for handler in app.logger.handlers[:]:
        app.logger.removeHandler(handler)

    app.logger.addHandler(RichPanelHandler(
        console=Console(stderr=True),
        show_time=True,
        show_level=True,
        markup=True
    ))

    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.handlers = []
    werkzeug_logger.addHandler(RichPanelHandler(
        console=Console(stderr=True),
        show_time=False,
        show_level=False,
        markup=True
    ))
    werkzeug_logger.setLevel(logging.WARNING)

    return app