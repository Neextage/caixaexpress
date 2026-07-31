"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : main.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Ponto de entrada principal do Caixa Express.
---------------------------------------------------------
"""

from config.constants import CONFIG_FILE, LOG_DIR
from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.logger_manager import LoggerManager
from ui.app import CaixaExpressApp


def main() -> None:
    """Inicializa os componentes principais da aplicação."""

    logger = LoggerManager(
        LOG_DIR
    )

    logger.info(
        "Inicializando Caixa Express."
    )

    config_manager = ConfigManager(
        CONFIG_FILE
    )

    database = DatabaseManager(
        logger
    )

    try:

        app = CaixaExpressApp(
            config_manager=config_manager,
            database=database,
            logger=logger,
        )

        app.run()

    finally:

        database.close()

        logger.info(
            "Sistema encerrado."
        )


if __name__ == "__main__":
    main()