"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : database.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pelo gerenciamento do banco de dados SQLite
do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from config.constants import DATABASE_FILE
from core.logger_manager import LoggerManager


class DatabaseManager:
    """Gerencia o banco de dados da aplicação."""

    def __init__(
        self,
        logger: LoggerManager,
    ) -> None:

        self._logger = logger
        self._database_path = DATABASE_FILE

        self._create_database_directory()

        self.connection = sqlite3.connect(
            self._database_path
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self._logger.info(
            "Banco de dados conectado."
        )

        self.create_tables()
        self.seed_default_recipients()

    def _create_database_directory(self) -> None:
        """Cria o diretório do banco caso não exista."""

        Path(
            self._database_path
        ).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def execute(
        self,
        query: str,
        parameters: tuple = (),
    ) -> None:
        """Executa um comando SQL."""

        self.cursor.execute(
            query,
            parameters,
        )

        self.connection.commit()

    def fetch_one(
        self,
        query: str,
        parameters: tuple = (),
    ):
        """Retorna um único registro."""

        self.cursor.execute(
            query,
            parameters,
        )

        return self.cursor.fetchone()

    def fetch_all(
        self,
        query: str,
        parameters: tuple = (),
    ):
        """Retorna vários registros."""

        self.cursor.execute(
            query,
            parameters,
        )

        return self.cursor.fetchall()

    def create_tables(self) -> None:
        """Cria todas as tabelas do sistema."""

        self._logger.info(
            "Criando tabelas..."
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS recipients(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                group_name TEXT NOT NULL,

                name TEXT NOT NULL,

                email TEXT NOT NULL UNIQUE,

                active INTEGER NOT NULL DEFAULT 1

            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                protocol TEXT,

                store_name TEXT,

                cash_value REAL,

                send_date TEXT,

                send_time TEXT,

                status TEXT,

                message TEXT

            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS settings(

                id INTEGER PRIMARY KEY,

                store_name TEXT,

                smtp_server TEXT,

                smtp_port INTEGER,

                sender_email TEXT,

                use_tls INTEGER,

                use_ssl INTEGER

            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                username TEXT,

                password_hash TEXT,

                role TEXT

            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                log_date TEXT,

                level TEXT,

                message TEXT

            )
            """
        )

        self.connection.commit()

        self._logger.info(
            "Tabelas criadas com sucesso."
        )

    # -----------------------------------------------------
    # DESTINATÁRIOS
    # -----------------------------------------------------

    def seed_default_recipients(self) -> None:
        """Cadastra os destinatários padrão."""

        recipients = [
            (
                "Financeiro",
                "Cleise",
                "cleise@admgto.com.br",
            ),
            (
                "Financeiro",
                "Financeiro",
                "financeiro@admgto.com.br",
            ),
            (
                "Supervisores",
                "Viviane",
                "viviane@admgto.com.br",
            ),
            (
                "Supervisores",
                "Faria",
                "faria@admgto.com.br",
            ),
            (
                "Diretoria",
                "Rene",
                "rene@admgto.com.br",
            ),
            (
                "Diretoria",
                "Rene Casa",
                "renecasa@admgto.com.br",
            ),
            (
                "TI",
                "Dylan Ryan",
                "dylanryan@admgto.com.br",
            ),
            (
                "TI",
                "Fabiano Galasso",
                "fabianogalasso@admgto.com.br",
            ),
        ]

        inserted = False

        for (
            group_name,
            name,
            email,
        ) in recipients:

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO recipients(
                    group_name,
                    name,
                    email,
                    active
                )
                VALUES (?, ?, ?, 1)
                """,
                (
                    group_name,
                    name,
                    email,
                ),
            )

            if self.cursor.rowcount > 0:
                inserted = True

        self.connection.commit()

        if inserted:
            self._logger.info(
                "Destinatários padrão cadastrados."
            )

    def get_all_recipients(self):
        """Retorna todos os destinatários."""

        return self.fetch_all(
            """
            SELECT
                id,
                group_name,
                name,
                email,
                active
            FROM recipients
            ORDER BY
                group_name,
                name
            """
        )

    def get_active_recipients(self):
        """Retorna somente destinatários ativos."""

        return self.fetch_all(
            """
            SELECT
                id,
                group_name,
                name,
                email,
                active
            FROM recipients
            WHERE active = 1
            ORDER BY
                group_name,
                name
            """
        )

    def add_recipient(
        self,
        group_name: str,
        name: str,
        email: str,
        active: bool = True,
    ) -> int:
        """Adiciona um destinatário."""

        self.cursor.execute(
            """
            INSERT INTO recipients(
                group_name,
                name,
                email,
                active
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                group_name,
                name,
                email,
                int(active),
            ),
        )

        self.connection.commit()

        return int(
            self.cursor.lastrowid
        )

    def update_recipient(
        self,
        recipient_id: int,
        group_name: str,
        name: str,
        email: str,
    ) -> None:
        """Atualiza um destinatário."""

        self.execute(
            """
            UPDATE recipients
            SET
                group_name = ?,
                name = ?,
                email = ?
            WHERE id = ?
            """,
            (
                group_name,
                name,
                email,
                recipient_id,
            ),
        )

    def delete_recipient(
        self,
        recipient_id: int,
    ) -> None:
        """Exclui um destinatário."""

        self.execute(
            """
            DELETE FROM recipients
            WHERE id = ?
            """,
            (
                recipient_id,
            ),
        )

    def set_recipient_active(
        self,
        recipient_id: int,
        active: bool,
    ) -> None:
        """Ativa ou desativa um destinatário."""

        self.execute(
            """
            UPDATE recipients
            SET active = ?
            WHERE id = ?
            """,
            (
                int(active),
                recipient_id,
            ),
        )

    # -----------------------------------------------------
    # HISTÓRICO
    # -----------------------------------------------------

    def add_history(
        self,
        protocol: str,
        store_name: str,
        cash_value: float,
        send_date: str,
        send_time: str,
        status: str,
        message: str,
    ) -> int:
        """Registra uma tentativa de envio."""

        self.cursor.execute(
            """
            INSERT INTO history(
                protocol,
                store_name,
                cash_value,
                send_date,
                send_time,
                status,
                message
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                protocol,
                store_name,
                cash_value,
                send_date,
                send_time,
                status,
                message,
            ),
        )

        self.connection.commit()

        history_id = int(
            self.cursor.lastrowid
        )

        self._logger.info(
            "Registro de histórico criado: "
            f"{protocol} - {status}"
        )

        return history_id

    def get_history(self):
        """Retorna o histórico de envios."""

        return self.fetch_all(
            """
            SELECT
                id,
                protocol,
                store_name,
                cash_value,
                send_date,
                send_time,
                status,
                message
            FROM history
            ORDER BY id DESC
            """
        )

    def get_history_summary(
        self,
    ) -> dict[str, int]:
        """Retorna indicadores do histórico."""

        rows = self.fetch_all(
            """
            SELECT
                status,
                COUNT(*) AS total
            FROM history
            GROUP BY status
            """
        )

        total = 0
        success = 0
        errors = 0

        for row in rows:

            count = int(
                row["total"]
            )

            total += count

            status = (
                row["status"]
                or ""
            ).strip().upper()

            if status in {
                "SUCESSO",
                "ENVIADO",
            }:
                success += count
            else:
                errors += count

        return {
            "total": total,
            "success": success,
            "errors": errors,
        }

    def close(self) -> None:
        """Encerra a conexão."""

        self.connection.close()

        self._logger.info(
            "Banco de dados encerrado."
        )