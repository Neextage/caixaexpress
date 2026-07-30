"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : main.py
---------------------------------------------------------
"""

from config.constants import CONFIG_FILE
from config.constants import LOG_DIR

from config.version import AppInfo

from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.logger_manager import LoggerManager


def main() -> None:

    logger = LoggerManager(LOG_DIR)

    logger.info("Inicializando Caixa Express.")

    config = ConfigManager(CONFIG_FILE)

    database = DatabaseManager(logger)

    print("=" * 50)

    print(AppInfo.NAME)

    print(f"Versão: {AppInfo.VERSION}")

    print(f"Loja: {config.store_name}")

    print("=" * 50)

    database.close()

    logger.info("Sistema encerrado.")


if __name__ == "__main__":
    main()