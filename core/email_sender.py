"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : email_sender.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela preparação e envio dos e-mails
de fechamento de caixa.
---------------------------------------------------------
"""

from __future__ import annotations

from email.message import EmailMessage
from email.utils import formataddr

from core.config_manager import ConfigManager
from core.html_builder import HTMLBuilder
from core.logger_manager import LoggerManager
from core.smtp_manager import SMTPManager


class EmailSender:
    """Prepara e envia os relatórios de fechamento."""

    def __init__(
        self,
        config_manager: ConfigManager,
        smtp_manager: SMTPManager,
        logger: LoggerManager,
    ) -> None:

        self._config_manager = config_manager
        self._smtp_manager = smtp_manager
        self._logger = logger

    def send_cash_report(
        self,
        store_name: str,
        cash_value: float,
        recipients: list[str],
    ) -> tuple[bool, str]:
        """Prepara e envia o relatório de fechamento."""

        clean_recipients = [
            email.strip()
            for email in recipients
            if email.strip()
        ]

        if not clean_recipients:
            return (
                False,
                "Nenhum destinatário ativo foi encontrado.",
            )

        if cash_value <= 0:
            return (
                False,
                "O valor do caixa precisa ser maior que zero.",
            )

        store_name = store_name.strip()

        if not store_name:
            return (
                False,
                "A loja não está configurada.",
            )

        try:

            self._config_manager.reload()

            sender = (
                self._config_manager.sender_email
            )

            if not sender:
                return (
                    False,
                    "O e-mail remetente não está configurado.",
                )

            html_content = (
                HTMLBuilder.build_cash_report(
                    store_name=store_name,
                    cash_value=cash_value,
                )
            )

            message = EmailMessage()

            message["Subject"] = (
                f"Fechamento de Caixa - {store_name}"
            )

            message["From"] = formataddr(
                (
                    "Caixa Express",
                    sender,
                )
            )

            message["To"] = ", ".join(
                clean_recipients
            )

            message.set_content(
                "Fechamento de Caixa\n\n"
                f"Loja: {store_name}\n"
                f"Valor: R$ {cash_value:,.2f}\n\n"
                "Esta mensagem possui uma versão "
                "HTML com o relatório completo."
            )

            message.add_alternative(
                html_content,
                subtype="html",
            )

            self._logger.info(
                "Relatório de fechamento preparado "
                f"para {len(clean_recipients)} "
                "destinatário(s)."
            )

            return self._smtp_manager.send_message(
                message
            )

        except Exception as error:

            technical_message = (
                f"{type(error).__name__}: {error}"
            )

            self._logger.error(
                "Falha na preparação do relatório - "
                f"{technical_message}"
            )

            return (
                False,
                "Não foi possível preparar "
                "o relatório de fechamento.",
            )