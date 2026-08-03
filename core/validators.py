"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : validators.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Centraliza validações reutilizáveis do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import re


class Validators:
    """Centraliza as regras de validação da aplicação."""

    EMAIL_PATTERN = re.compile(
        r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )

    @staticmethod
    def is_valid_store_name(
        store_name: str,
    ) -> bool:
        """Valida o nome da loja."""

        return bool(
            store_name.strip()
        )

    @classmethod
    def is_valid_email(
        cls,
        email: str,
    ) -> bool:
        """Valida um endereço de e-mail."""

        email = email.strip()

        if not email:
            return False

        return bool(
            cls.EMAIL_PATTERN.fullmatch(
                email
            )
        )

    @staticmethod
    def is_valid_smtp_server(
        smtp_server: str,
    ) -> bool:
        """Valida se o servidor SMTP foi informado."""

        return bool(
            smtp_server.strip()
        )

    @staticmethod
    def is_valid_port(
        port: str | int,
    ) -> bool:
        """Valida uma porta TCP."""

        try:
            value = int(port)

        except (
            TypeError,
            ValueError,
        ):
            return False

        return 1 <= value <= 65535

    @staticmethod
    def is_valid_timeout(
        timeout: str | int,
    ) -> bool:
        """Valida o timeout da conexão."""

        try:
            value = int(timeout)

        except (
            TypeError,
            ValueError,
        ):
            return False

        return value > 0

    @staticmethod
    def is_valid_cash_value(
        cash_value: float,
    ) -> bool:
        """Valida o valor do fechamento."""

        try:
            value = float(
                cash_value
            )

        except (
            TypeError,
            ValueError,
        ):
            return False

        return value > 0

    @classmethod
    def clean_recipients(
        cls,
        recipients: list[str],
    ) -> list[str]:
        """
        Remove destinatários vazios e mantém
        somente endereços de e-mail válidos.
        """

        clean: list[str] = []

        for email in recipients:

            email = email.strip()

            if not cls.is_valid_email(
                email
            ):
                continue

            if email not in clean:
                clean.append(
                    email
                )

        return clean

    @staticmethod
    def is_valid_security_mode(
        use_tls: bool,
        use_ssl: bool,
    ) -> bool:
        """Impede TLS e SSL simultâneos."""

        return not (
            use_tls
            and use_ssl
        )