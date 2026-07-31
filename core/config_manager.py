"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : config_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela leitura, alteração e gravação das
configurações do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path
from typing import Any


class ConfigManager:
    """Gerencia o arquivo config.ini da aplicação."""

    def __init__(self, config_file: Path) -> None:
        self.config_file = Path(config_file)
        self.config = ConfigParser()

        self.load()

    def load(self) -> None:
        """Carrega as configurações do arquivo."""

        if not self.config_file.exists():
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: "
                f"{self.config_file}"
            )

        self.config.read(
            self.config_file,
            encoding="utf-8",
        )

    def reload(self) -> None:
        """Recarrega as configurações."""

        self.config.clear()
        self.load()

    def save(self) -> None:
        """Salva as configurações no arquivo."""

        self.config_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.config_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            self.config.write(file)

    def get(
        self,
        section: str,
        option: str,
        fallback: Any = None,
    ) -> str | Any:
        """Obtém uma configuração."""

        return self.config.get(
            section,
            option,
            fallback=fallback,
        )

    def get_int(
        self,
        section: str,
        option: str,
        fallback: int = 0,
    ) -> int:
        """Obtém uma configuração inteira."""

        return self.config.getint(
            section,
            option,
            fallback=fallback,
        )

    def get_bool(
        self,
        section: str,
        option: str,
        fallback: bool = False,
    ) -> bool:
        """Obtém uma configuração booleana."""

        return self.config.getboolean(
            section,
            option,
            fallback=fallback,
        )

    def set(
        self,
        section: str,
        option: str,
        value: Any,
    ) -> None:
        """Altera uma configuração."""

        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(
            section,
            option,
            str(value),
        )

    @property
    def store_name(self) -> str:
        """Retorna o nome configurado da loja."""

        return self.get(
            "LOJA",
            "NOME_LOJA",
            "",
        ).strip()

    @property
    def smtp_server(self) -> str:
        """Retorna o servidor SMTP."""

        return self.get(
            "EMAIL",
            "SMTP_SERVER",
            "",
        ).strip()

    @property
    def smtp_port(self) -> int:
        """Retorna a porta SMTP."""

        return self.get_int(
            "EMAIL",
            "SMTP_PORT",
            587,
        )

    @property
    def sender_email(self) -> str:
        """Retorna o endereço remetente."""

        return self.get(
            "EMAIL",
            "EMAIL_REMETENTE",
            "",
        ).strip()

    @property
    def password(self) -> str:
        """Retorna a senha SMTP."""

        return self.get(
            "EMAIL",
            "SENHA",
            "",
        )

    @property
    def use_tls(self) -> bool:
        """Informa se TLS está habilitado."""

        return self.get_bool(
            "EMAIL",
            "TLS",
            True,
        )

    @property
    def use_ssl(self) -> bool:
        """Informa se SSL está habilitado."""

        return self.get_bool(
            "EMAIL",
            "SSL",
            False,
        )

    @property
    def timeout(self) -> int:
        """Retorna o timeout SMTP."""

        return self.get_int(
            "EMAIL",
            "TIMEOUT",
            30,
        )