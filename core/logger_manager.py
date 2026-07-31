"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : logger_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela geração, armazenamento e leitura
dos logs do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import logging
from pathlib import Path


class LoggerManager:
    """Gerencia os logs da aplicação."""

    LOG_FILENAME = "caixaexpress.log"

    def __init__(
        self,
        log_directory: Path,
    ) -> None:

        self.log_directory = Path(
            log_directory
        )

        self.log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.log_file = (
            self.log_directory
            / self.LOG_FILENAME
        )

        self.logger = logging.getLogger(
            "CaixaExpress"
        )

        self.logger.setLevel(
            logging.INFO
        )

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8",
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(
                formatter
            )

            self.logger.addHandler(
                file_handler
            )

            self.logger.addHandler(
                console_handler
            )

    def info(
        self,
        message: str,
    ) -> None:
        """Registra uma informação."""

        self.logger.info(
            message
        )

    def warning(
        self,
        message: str,
    ) -> None:
        """Registra um aviso."""

        self.logger.warning(
            message
        )

    def error(
        self,
        message: str,
    ) -> None:
        """Registra um erro."""

        self.logger.error(
            message
        )

    def read_logs(
        self,
        level: str = "TODOS",
        limit: int = 500,
    ) -> list[str]:
        """
        Lê os registros mais recentes do arquivo de log.

        level:
            TODOS
            INFO
            WARNING
            ERROR
        """

        if not self.log_file.exists():
            return []

        try:
            with self.log_file.open(
                "r",
                encoding="utf-8",
            ) as file:
                lines = [
                    line.rstrip("\n")
                    for line in file
                    if line.strip()
                ]

        except (
            OSError,
            UnicodeError,
        ) as error:

            self.error(
                "Erro ao ler arquivo de logs: "
                f"{error}"
            )

            return []

        selected_level = (
            level.strip().upper()
        )

        if selected_level != "TODOS":

            marker = (
                f"| {selected_level} |"
            )

            lines = [
                line
                for line in lines
                if marker in line
            ]

        if limit > 0:
            lines = lines[-limit:]

        # Mais recentes primeiro.
        lines.reverse()

        return lines

    def get_log_counts(
        self,
    ) -> dict[str, int]:
        """Retorna contadores por nível."""

        logs = self.read_logs(
            level="TODOS",
            limit=0,
        )

        counts = {
            "total": len(logs),
            "info": 0,
            "warning": 0,
            "error": 0,
        }

        for line in logs:

            if "| INFO |" in line:
                counts["info"] += 1

            elif "| WARNING |" in line:
                counts["warning"] += 1

            elif "| ERROR |" in line:
                counts["error"] += 1

        return counts