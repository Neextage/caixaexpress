"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : main.py
---------------------------------------------------------
"""
from ui.app import CaixaExpressApp
from config.constants import CONFIG_FILE
from config.constants import LOG_DIR

from config.version import AppInfo

from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.logger_manager import LoggerManager


def main() -> None:

    logger = LoggerManager(LOG_DIR)

    logger.info("Inicializando Caixa Express.")

    ConfigManager(CONFIG_FILE)

    DatabaseManager(logger)

    app = CaixaExpressApp()

    app.run()

    logger.info("Sistema encerrado.")


if __name__ == "__main__":
    main()