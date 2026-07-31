"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : tests_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Página administrativa para testes da configuração
SMTP e envio de e-mails do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import threading

import customtkinter as ctk

from config.theme import ThemeColors
from core.config_manager import ConfigManager
from core.smtp_manager import SMTPManager


class TestsPage(ctk.CTkFrame):
    """Página administrativa de testes."""

    def __init__(
        self,
        master,
        config_manager: ConfigManager,
        smtp_manager: SMTPManager,
    ) -> None:

        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._config_manager = (
            config_manager
        )

        self._smtp_manager = (
            smtp_manager
        )

        self._test_running = False

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria a interface."""

        self._create_header()
        self._create_smtp_information()
        self._create_connection_test()
        self._create_email_test()

    def _create_header(self) -> None:
        """Cria o cabeçalho."""

        header = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        header.pack(
            fill="x",
            padx=45,
            pady=(40, 20),
        )

        title = ctk.CTkLabel(
            header,
            text="Testes",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
        )

        description = ctk.CTkLabel(
            header,
            text=(
                "Verifique a configuração SMTP "
                "e realize envios de teste."
            ),
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            pady=(4, 0),
        )

    def _create_smtp_information(
        self,
    ) -> None:
        """Cria o cartão de informações SMTP."""

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            padx=45,
            pady=(0, 15),
        )

        title = ctk.CTkLabel(
            card,
            text="Configuração atual",
            font=("Segoe UI", 16, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=22,
            pady=(18, 10),
        )

        self.server_label = ctk.CTkLabel(
            card,
            text="Servidor: -",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT,
        )

        self.server_label.pack(
            anchor="w",
            padx=22,
            pady=2,
        )

        self.port_label = ctk.CTkLabel(
            card,
            text="Porta: -",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT,
        )

        self.port_label.pack(
            anchor="w",
            padx=22,
            pady=2,
        )

        self.sender_label = ctk.CTkLabel(
            card,
            text="Remetente: -",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT,
        )

        self.sender_label.pack(
            anchor="w",
            padx=22,
            pady=2,
        )

        self.security_label = ctk.CTkLabel(
            card,
            text="Segurança: -",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT,
        )

        self.security_label.pack(
            anchor="w",
            padx=22,
            pady=(2, 18),
        )

    def _create_connection_test(
        self,
    ) -> None:
        """Cria o teste de conexão."""

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            padx=45,
            pady=(0, 15),
        )

        title = ctk.CTkLabel(
            card,
            text="Teste de conexão SMTP",
            font=("Segoe UI", 16, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=22,
            pady=(18, 5),
        )

        description = ctk.CTkLabel(
            card,
            text=(
                "Testa conexão, segurança e "
                "autenticação sem enviar e-mail."
            ),
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            padx=22,
        )

        self.connection_status = (
            ctk.CTkLabel(
                card,
                text="",
                font=(
                    "Segoe UI",
                    12,
                    "bold",
                ),
                text_color=(
                    ThemeColors.TEXT_LIGHT
                ),
            )
        )

        self.connection_status.pack(
            anchor="w",
            padx=22,
            pady=(12, 5),
        )

        self.connection_button = (
            ctk.CTkButton(
                card,
                text="TESTAR CONEXÃO SMTP",
                height=42,
                corner_radius=8,
                fg_color=ThemeColors.PRIMARY,
                hover_color="#26356F",
                command=(
                    self._start_connection_test
                ),
            )
        )

        self.connection_button.pack(
            fill="x",
            padx=22,
            pady=(5, 20),
        )

    def _create_email_test(
        self,
    ) -> None:
        """Cria o teste de envio."""

        card = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            padx=45,
            pady=(0, 30),
        )

        title = ctk.CTkLabel(
            card,
            text="Enviar e-mail de teste",
            font=("Segoe UI", 16, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=22,
            pady=(18, 5),
        )

        description = ctk.CTkLabel(
            card,
            text=(
                "Informe um endereço para receber "
                "uma mensagem de teste."
            ),
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            padx=22,
        )

        self.recipient_entry = (
            ctk.CTkEntry(
                card,
                height=42,
                placeholder_text=(
                    "E-mail de destino"
                ),
                font=("Segoe UI", 13),
            )
        )

        self.recipient_entry.pack(
            fill="x",
            padx=22,
            pady=(15, 10),
        )

        self.email_status = ctk.CTkLabel(
            card,
            text="",
            font=(
                "Segoe UI",
                12,
                "bold",
            ),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        self.email_status.pack(
            anchor="w",
            padx=22,
            pady=(0, 5),
        )

        self.email_button = ctk.CTkButton(
            card,
            text="ENVIAR E-MAIL DE TESTE",
            height=42,
            corner_radius=8,
            fg_color=ThemeColors.SECONDARY,
            hover_color="#692027",
            command=self._start_email_test,
        )

        self.email_button.pack(
            fill="x",
            padx=22,
            pady=(5, 20),
        )

    def refresh(self) -> None:
        """Atualiza as informações da tela."""

        self._config_manager.reload()

        self.server_label.configure(
            text=(
                "Servidor: "
                f"{self._config_manager.smtp_server or '-'}"
            )
        )

        self.port_label.configure(
            text=(
                "Porta: "
                f"{self._config_manager.smtp_port}"
            )
        )

        self.sender_label.configure(
            text=(
                "Remetente: "
                f"{self._config_manager.sender_email or '-'}"
            )
        )

        if self._config_manager.use_ssl:
            security = "SSL"

        elif self._config_manager.use_tls:
            security = "TLS"

        else:
            security = "Sem TLS/SSL"

        self.security_label.configure(
            text=(
                f"Segurança: {security}"
            )
        )

    def _set_running(
        self,
        running: bool,
    ) -> None:
        """Controla os botões durante testes."""

        self._test_running = running

        state = (
            "disabled"
            if running
            else "normal"
        )

        self.connection_button.configure(
            state=state
        )

        self.email_button.configure(
            state=state
        )

    def _start_connection_test(
        self,
    ) -> None:
        """Inicia o teste SMTP."""

        if self._test_running:
            return

        self._set_running(
            True
        )

        self.connection_status.configure(
            text=(
                "Testando conexão com "
                "o servidor..."
            ),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        thread = threading.Thread(
            target=self._run_connection_test,
            daemon=True,
        )

        thread.start()

    def _run_connection_test(
        self,
    ) -> None:
        """Executa o teste fora da interface."""

        success, message = (
            self._smtp_manager
            .test_connection()
        )

        self.after(
            0,
            lambda: (
                self._finish_connection_test(
                    success,
                    message,
                )
            ),
        )

    def _finish_connection_test(
        self,
        success: bool,
        message: str,
    ) -> None:
        """Finaliza o teste de conexão."""

        color = (
            ThemeColors.SUCCESS
            if success
            else ThemeColors.ERROR
        )

        self.connection_status.configure(
            text=message,
            text_color=color,
        )

        self._set_running(
            False
        )

    def _start_email_test(
        self,
    ) -> None:
        """Inicia um envio de teste."""

        if self._test_running:
            return

        recipient = (
            self.recipient_entry
            .get()
            .strip()
        )

        if not recipient:

            self.email_status.configure(
                text=(
                    "Informe o e-mail "
                    "de destino."
                ),
                text_color=ThemeColors.ERROR,
            )

            return

        self._set_running(
            True
        )

        self.email_status.configure(
            text="Enviando e-mail de teste...",
            text_color=ThemeColors.TEXT_LIGHT,
        )

        thread = threading.Thread(
            target=self._run_email_test,
            args=(recipient,),
            daemon=True,
        )

        thread.start()

    def _run_email_test(
        self,
        recipient: str,
    ) -> None:
        """Executa o envio fora da interface."""

        success, message = (
            self._smtp_manager
            .send_test_email(
                recipient
            )
        )

        self.after(
            0,
            lambda: (
                self._finish_email_test(
                    success,
                    message,
                )
            ),
        )

    def _finish_email_test(
        self,
        success: bool,
        message: str,
    ) -> None:
        """Finaliza o envio de teste."""

        color = (
            ThemeColors.SUCCESS
            if success
            else ThemeColors.ERROR
        )

        self.email_status.configure(
            text=message,
            text_color=color,
        )

        self._set_running(
            False
        )