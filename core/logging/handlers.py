from rich.theme import Theme # type: ignore
from rich.console import Console # type: ignore
from rich.logging import RichHandler # type: ignore

class FlaskRichHandler(RichHandler):
    """Handler personalizado para Flask"""

    def __init__(self):
        flask_theme = Theme({
            "info": "dim cyan",
            "warning": "magenta",
            "error": "bold red",
            "critical": "bold white on red",
            "request": "bold bright_blue",
            "response": "bold green"
        })

        super().__init__(
            console=Console(theme=flask_theme),
            show_time=True,
            show_level=True,
            show_path=False,
            rich_tracebacks=True
        )