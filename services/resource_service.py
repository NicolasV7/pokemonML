import pickle
import logging
import pandas as pd # type: ignore
from rich.text import Text # type: ignore
from rich.panel import Panel # type: ignore
from rich.table import Table # type: ignore
from rich.progress import track # type: ignore
from rich.console import Console # type: ignore
from core.cluster_config import BASE_CLUSTER_INFO


class ResourceService:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = None
        self.df = None
        self.cluster_info = None
        self.console = Console()
        self.logger = logging.getLogger('services.resource')

    def _log_success(self, message):
        """Log de éxito con formato visual"""
        self.console.print(
            Panel.fit(
                Text.from_markup(f"[green]✓ {message}[/]"),
                border_style="green"
            )
        )
        self.logger.info(message)

    def _log_loading(self, message):
        """Log de proceso de carga"""
        self.console.print(
            Panel.fit(
                Text.from_markup(f"[cyan]⌛ {message}[/]"),
                border_style="blue"
            )
        )
        self.logger.debug(message)

    def _log_error(self, message, exception=None):
        """Log de error con formato visual"""
        self.console.print(
            Panel.fit(
                Text.from_markup(f"[red]✗ {message}[/]"),
                border_style="red"
            )
        )
        if exception:
            self.console.print_exception()
        self.logger.error(message, exc_info=exception is not None)

    def load_model(self):
        self._log_loading("Cargando modelo KMeans...")
        try:
            with open(self.config['MODEL_PATH'], 'rb') as f:
                self.model = pickle.load(f)
            self._log_success("Modelo KMeans cargado correctamente")
        except Exception as e:
            self._log_error("Error cargando modelo KMeans", e)
            raise

    def load_scaler(self):
        self._log_loading("Cargando scaler...")
        try:
            with open(self.config['SCALER_PATH'], 'rb') as f:
                self.scaler = pickle.load(f)
            self._log_success("Scaler cargado correctamente")
        except Exception as e:
            self._log_error("Error cargando scaler", e)
            raise

    def load_data(self):
        self._log_loading("Cargando dataset Pokémon...")
        try:
            self.df = pd.read_csv(self.config['DATA_PATH'])

            table = Table(title="Resumen del Dataset")
            table.add_column("Columnas", style="cyan")
            table.add_column("Registros", style="magenta")
            table.add_row(str(len(self.df.columns)), str(len(self.df)))

            self.console.print(table)
            self._log_success(f"Dataset cargado correctamente (registros: {len(self.df)})")
        except Exception as e:
            self._log_error("Error cargando dataset", e)
            raise

    def process_cluster_info(self):
        self._log_loading("Procesando información de clusters...")
        try:
            self.cluster_info = BASE_CLUSTER_INFO.copy()

            for cluster_id in track(
                self.cluster_info.keys(),
                description="Procesando clusters..."
            ):
                ejemplos_con_imagenes = []
                for name in self.cluster_info[cluster_id]['ejemplos']:
                    pokemon = self.df[self.df['Name'] == name]
                    if not pokemon.empty:
                        numero = pokemon.iloc[0]['#']
                        ejemplos_con_imagenes.append({
                            'name': name,
                            'image': f"{numero:03d}.png"
                        })
                self.cluster_info[cluster_id]['ejemplos'] = ejemplos_con_imagenes

            # Mostrar resumen de clusters
            cluster_table = Table(title="Clusters Procesados")
            cluster_table.add_column("Cluster ID", style="cyan")
            cluster_table.add_column("Nombre", style="green")
            cluster_table.add_column("Ejemplos", style="yellow")

            for cluster_id, info in self.cluster_info.items():
                examples = "\n".join([e['name'] for e in info['ejemplos']])
                cluster_table.add_row(
                    str(cluster_id),
                    info['nombre'],
                    examples
                )

            self.console.print(cluster_table)
            self._log_success("Información de clusters procesada")

        except Exception as e:
            self._log_error("Error procesando clusters", e)
            raise

    def load_all_resources(self):
        try:
            self.console.print(
                Panel.fit(
                    Text.from_markup(
                        "[bold blue]Iniciando carga de recursos Pokémon[/]\n"
                        "[bold]Configuración:[/]\n"
                        f"• Modelo: {self.config['MODEL_PATH']}\n"
                        f"• Scaler: {self.config['SCALER_PATH']}\n"
                        f"• Dataset: {self.config['DATA_PATH']}"
                    ),
                    border_style="blue",
                    padding=(1, 4)
                )
            )
            self.logger.info("Iniciando carga de recursos...")

            self.load_model()
            self.load_scaler()
            self.load_data()
            self.process_cluster_info()

            self.console.print(
                Panel.fit(
                    Text.from_markup("[bold green]🎉 Todos los recursos cargados exitosamente[/]"),
                    border_style="green",
                    padding=(1, 4)
                )
            )
            self.logger.info("Todos los recursos cargados exitosamente")
            return True

        except Exception as e:
            self._log_error("Error crítico cargando recursos", e)
            raise