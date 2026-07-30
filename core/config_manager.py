"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : config_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
"""

from configparser import ConfigParser
from pathlib import Path


class ConfigManager:
    """Responsável por gerenciar o arquivo config.ini."""

    def __init__(self, config_file: Path):
        self.config_file = config_file
        self.config = ConfigParser()

        self.load()

    def load(self):
        """Carrega o arquivo de configuração."""

        self.config.read(
            self.config_file,
            encoding="utf-8"
        )

    def save(self):
        """Salva as configurações."""

        with open(
            self.config_file,
            "w",
            encoding="utf-8"
        ) as file:
            self.config.write(file)

    def get(self, section: str, option: str, fallback=None):
        """Obtém um valor."""

        return self.config.get(
            section,
            option,
            fallback=fallback
        )

    def get_int(self, section: str, option: str, fallback=0):

        return self.config.getint(
            section,
            option,
            fallback=fallback
        )

    def get_bool(self, section: str, option: str, fallback=False):

        return self.config.getboolean(
            section,
            option,
            fallback=fallback
        )

    def set(self, section: str, option: str, value):

        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(
            section,
            option,
            str(value)
        )

    @property
    def store_name(self):

        return self.get("LOJA", "NOME_LOJA")

    @property
    def smtp_server(self):

        return self.get("EMAIL", "SMTP_SERVER")

    @property
    def smtp_port(self):

        return self.get_int("EMAIL", "SMTP_PORT")

    @property
    def sender_email(self):

        return self.get("EMAIL", "EMAIL_REMETENTE")

    @property
    def password(self):

        return self.get("EMAIL", "SENHA")