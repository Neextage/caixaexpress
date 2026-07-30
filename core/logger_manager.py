"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : logger_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
"""

import logging

from pathlib import Path


class LoggerManager:

    def __init__(self, log_directory: Path):

        self.log_directory = log_directory

        self.log_directory.mkdir(
            exist_ok=True
        )

        self.logger = logging.getLogger("CaixaExpress")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                self.log_directory / "caixaexpress.log",
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

            self.logger.addHandler(console_handler)

    def info(self, message: str):

        self.logger.info(message)

    def warning(self, message: str):

        self.logger.warning(message)

    def error(self, message: str):

        self.logger.error(message)