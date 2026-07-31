"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : smtp_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela conexão, autenticação e comunicação
com servidores SMTP.
---------------------------------------------------------
"""

from __future__ import annotations

import smtplib
import socket
import ssl
from email.message import EmailMessage

from core.config_manager import ConfigManager
from core.logger_manager import LoggerManager


class SMTPManager:
    """Gerencia a comunicação SMTP do Caixa Express."""

    def __init__(
        self,
        config_manager: ConfigManager,
        logger: LoggerManager,
    ) -> None:

        self._config_manager = config_manager
        self._logger = logger

    def _reload_configuration(self) -> None:
        """Recarrega o config.ini antes da operação."""

        self._config_manager.reload()

    def _validate_configuration(self) -> None:
        """Valida as configurações mínimas do SMTP."""

        if not self._config_manager.smtp_server:
            raise ValueError(
                "Servidor SMTP não configurado."
            )

        if not self._config_manager.smtp_port:
            raise ValueError(
                "Porta SMTP não configurada."
            )

        if not self._config_manager.sender_email:
            raise ValueError(
                "E-mail remetente não configurado."
            )

        if not self._config_manager.password:
            raise ValueError(
                "Senha SMTP não configurada."
            )

        if (
            self._config_manager.use_tls
            and self._config_manager.use_ssl
        ):
            raise ValueError(
                "TLS e SSL não podem estar "
                "ativos simultaneamente."
            )

    def _connect(self):
        """Abre e autentica uma conexão SMTP."""

        server_address = (
            self._config_manager.smtp_server
        )

        port = (
            self._config_manager.smtp_port
        )

        timeout = (
            self._config_manager.timeout
        )

        sender = (
            self._config_manager.sender_email
        )

        password = (
            self._config_manager.password
        )

        context = (
            ssl.create_default_context()
        )

        if self._config_manager.use_ssl:

            smtp = smtplib.SMTP_SSL(
                server_address,
                port,
                timeout=timeout,
                context=context,
            )

        else:

            smtp = smtplib.SMTP(
                server_address,
                port,
                timeout=timeout,
            )

            smtp.ehlo()

            if self._config_manager.use_tls:

                smtp.starttls(
                    context=context
                )

                smtp.ehlo()

        smtp.login(
            sender,
            password,
        )

        return smtp

    def test_connection(
        self,
    ) -> tuple[bool, str]:
        """Testa conexão e autenticação SMTP."""

        smtp = None

        try:

            self._reload_configuration()
            self._validate_configuration()

            self._logger.info(
                "Iniciando teste de conexão SMTP."
            )

            smtp = self._connect()

            self._logger.info(
                "Teste SMTP concluído com sucesso."
            )

            return (
                True,
                "Conexão e autenticação SMTP "
                "realizadas com sucesso.",
            )

        except Exception as error:

            technical_message = (
                f"{type(error).__name__}: {error}"
            )

            self._logger.error(
                "Falha no teste SMTP - "
                f"{technical_message}"
            )

            return (
                False,
                self._friendly_error(error),
            )

        finally:

            if smtp is not None:

                try:
                    smtp.quit()

                except Exception:
                    pass

    def send_test_email(
        self,
        recipient: str,
    ) -> tuple[bool, str]:
        """Envia um e-mail de teste."""

        smtp = None

        recipient = recipient.strip()

        if not self._is_valid_email(
            recipient
        ):
            return (
                False,
                "Informe um e-mail de destino válido.",
            )

        try:

            self._reload_configuration()
            self._validate_configuration()

            sender = (
                self._config_manager.sender_email
            )

            store_name = (
                self._config_manager.store_name
                or "Loja não configurada"
            )

            message = EmailMessage()

            message["Subject"] = (
                "Caixa Express - Teste de E-mail"
            )

            message["From"] = sender
            message["To"] = recipient

            message.set_content(
                "Teste de envio realizado pelo "
                "Caixa Express.\n\n"
                f"Loja configurada: {store_name}\n\n"
                "Se você recebeu esta mensagem, "
                "a configuração de envio de e-mail "
                "está funcionando corretamente.\n\n"
                "Esta é uma mensagem de teste."
            )

            self._logger.info(
                "Iniciando envio de e-mail de teste "
                f"para {recipient}."
            )

            smtp = self._connect()

            smtp.send_message(
                message
            )

            self._logger.info(
                "E-mail de teste enviado com sucesso "
                f"para {recipient}."
            )

            return (
                True,
                "E-mail de teste enviado com sucesso.",
            )

        except Exception as error:

            technical_message = (
                f"{type(error).__name__}: {error}"
            )

            self._logger.error(
                "Falha no envio de e-mail de teste - "
                f"{technical_message}"
            )

            return (
                False,
                self._friendly_error(error),
            )

        finally:

            if smtp is not None:

                try:
                    smtp.quit()

                except Exception:
                    pass

    def send_message(
        self,
        message: EmailMessage,
    ) -> tuple[bool, str]:
        """Envia uma mensagem de e-mail já preparada."""

        smtp = None

        try:

            self._reload_configuration()
            self._validate_configuration()

            recipients = message.get_all(
                "To",
                [],
            )

            if not recipients:
                return (
                    False,
                    "Nenhum destinatário foi informado.",
                )

            self._logger.info(
                "Iniciando envio de mensagem SMTP."
            )

            smtp = self._connect()

            smtp.send_message(
                message
            )

            self._logger.info(
                "Mensagem SMTP enviada com sucesso."
            )

            return (
                True,
                "Mensagem enviada com sucesso.",
            )

        except Exception as error:

            technical_message = (
                f"{type(error).__name__}: {error}"
            )

            self._logger.error(
                "Falha no envio da mensagem SMTP - "
                f"{technical_message}"
            )

            return (
                False,
                self._friendly_error(error),
            )

        finally:

            if smtp is not None:

                try:
                    smtp.quit()

                except Exception:
                    pass

    @staticmethod
    def _is_valid_email(
        email: str,
    ) -> bool:
        """Realiza validação básica do e-mail."""

        if not email:
            return False

        if "@" not in email:
            return False

        local_part, _, domain = (
            email.rpartition("@")
        )

        if not local_part:
            return False

        if not domain:
            return False

        if "." not in domain:
            return False

        return True

    @staticmethod
    def _friendly_error(
        error: Exception,
    ) -> str:
        """Converte erros técnicos em mensagens amigáveis."""

        if isinstance(
            error,
            smtplib.SMTPAuthenticationError,
        ):
            return (
                "Não foi possível autenticar no "
                "servidor de e-mail. Verifique o "
                "remetente e a senha SMTP."
            )

        if isinstance(
            error,
            smtplib.SMTPConnectError,
        ):
            return (
                "Não foi possível estabelecer conexão "
                "com o servidor de e-mail."
            )

        if isinstance(
            error,
            smtplib.SMTPRecipientsRefused,
        ):
            return (
                "O servidor recusou o e-mail "
                "de destino informado."
            )

        if isinstance(
            error,
            smtplib.SMTPSenderRefused,
        ):
            return (
                "O servidor recusou o "
                "e-mail remetente."
            )

        if isinstance(
            error,
            smtplib.SMTPServerDisconnected,
        ):
            return (
                "A conexão com o servidor de e-mail "
                "foi encerrada inesperadamente."
            )

        if isinstance(
            error,
            socket.timeout,
        ):
            return (
                "O servidor de e-mail demorou demais "
                "para responder."
            )

        if isinstance(
            error,
            socket.gaierror,
        ):
            return (
                "Não foi possível localizar o "
                "servidor de e-mail."
            )

        if isinstance(
            error,
            ssl.SSLError,
        ):
            return (
                "Ocorreu uma falha de segurança "
                "SSL/TLS durante a conexão."
            )

        if isinstance(
            error,
            ConnectionRefusedError,
        ):
            return (
                "A conexão com o servidor de e-mail "
                "foi recusada."
            )

        if isinstance(
            error,
            ValueError,
        ):
            return str(error)

        return (
            "Não foi possível concluir a operação "
            "com o servidor de e-mail."
        )