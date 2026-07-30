"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : database.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pelo gerenciamento do banco de dados SQLite.
---------------------------------------------------------
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from config.constants import DATABASE_FILE
from core.logger_manager import LoggerManager


class DatabaseManager:
    """Gerencia o banco de dados da aplicação."""

    def __init__(self, logger: LoggerManager) -> None:
        self._logger = logger

        self._database_path = DATABASE_FILE

        self._create_database_directory()

        self.connection = sqlite3.connect(self._database_path)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self._logger.info("Banco de dados conectado.")

        self.create_tables()

    def _create_database_directory(self) -> None:
        """Cria o diretório do banco caso não exista."""

        Path(self._database_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def execute(
        self,
        query: str,
        parameters: tuple = ()
    ) -> None:
        """Executa comandos SQL."""

        self.cursor.execute(query, parameters)

        self.connection.commit()

    def fetch_one(
        self,
        query: str,
        parameters: tuple = ()
    ):
        """Retorna um único registro."""

        self.cursor.execute(query, parameters)

        return self.cursor.fetchone()

    def fetch_all(
        self,
        query: str,
        parameters: tuple = ()
    ):
        """Retorna vários registros."""

        self.cursor.execute(query, parameters)

        return self.cursor.fetchall()

    def create_tables(self) -> None:
        """Cria todas as tabelas do sistema."""

        self._logger.info("Criando tabelas...")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipients(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            group_name TEXT NOT NULL,

            name TEXT NOT NULL,

            email TEXT NOT NULL UNIQUE,

            active INTEGER NOT NULL DEFAULT 1

        )
        """)

        self.cursor.execute("""
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
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(

            id INTEGER PRIMARY KEY,

            store_name TEXT,

            smtp_server TEXT,

            smtp_port INTEGER,

            sender_email TEXT,

            use_tls INTEGER,

            use_ssl INTEGER

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            password_hash TEXT,

            role TEXT

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            log_date TEXT,

            level TEXT,

            message TEXT

        )
        """)

        self.connection.commit()

        self._logger.info("Tabelas criadas com sucesso.")

    def close(self) -> None:
        """Encerra a conexão."""

        self.connection.close()

        self._logger.info("Banco de dados encerrado.")