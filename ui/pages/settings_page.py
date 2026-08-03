"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : settings_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Página administrativa responsável pelas configurações
gerais e de SMTP do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from core.config_manager import ConfigManager
from config.theme import ThemeColors
from core.config_manager import ConfigManager
from core.validators import Validators


class SettingsPage(ctk.CTkFrame):
    """Página de configurações do Caixa Express."""

    def __init__(
        self,
        master,
        config_manager: ConfigManager,
    ) -> None:
        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._config_manager = config_manager

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria os componentes da página."""

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
            text="Configuração",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
        )

        description = ctk.CTkLabel(
            header,
            text=(
                "Configure a loja e os dados utilizados "
                "para envio dos relatórios."
            ),
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            pady=(4, 0),
        )

        self.content_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
        )

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=(0, 25),
        )

        self._create_store_section()
        self._create_smtp_section()
        self._create_save_area()

    def _create_store_section(self) -> None:
        """Cria a seção de configuração da loja."""

        card = ctk.CTkFrame(
            self.content_frame,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            pady=(0, 15),
        )

        title = ctk.CTkLabel(
            card,
            text="Identificação da Loja",
            font=("Segoe UI", 17, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15),
        )

        label = ctk.CTkLabel(
            card,
            text="Nome da loja",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        label.pack(
            anchor="w",
            padx=25,
        )

        self.store_entry = ctk.CTkEntry(
            card,
            height=42,
            placeholder_text="Ex.: EXTRA ANCHIETA",
            font=("Segoe UI", 13),
        )

        self.store_entry.pack(
            fill="x",
            padx=25,
            pady=(5, 25),
        )

    def _create_smtp_section(self) -> None:
        """Cria a seção de configuração SMTP."""

        card = ctk.CTkFrame(
            self.content_frame,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            pady=(0, 15),
        )

        title = ctk.CTkLabel(
            card,
            text="Envio de E-mail",
            font=("Segoe UI", 17, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 15),
        )

        fields_frame = ctk.CTkFrame(
            card,
            fg_color="transparent",
        )

        fields_frame.pack(
            fill="x",
            padx=25,
        )

        fields_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        fields_frame.grid_columnconfigure(
            1,
            weight=1,
        )

        server_label = ctk.CTkLabel(
            fields_frame,
            text="Servidor SMTP",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        server_label.grid(
            row=0,
            column=0,
            sticky="w",
        )

        port_label = ctk.CTkLabel(
            fields_frame,
            text="Porta",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        port_label.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(10, 0),
        )

        self.smtp_server_entry = ctk.CTkEntry(
            fields_frame,
            height=42,
            font=("Segoe UI", 13),
        )

        self.smtp_server_entry.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(5, 15),
        )

        self.smtp_port_entry = ctk.CTkEntry(
            fields_frame,
            height=42,
            font=("Segoe UI", 13),
        )

        self.smtp_port_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=(10, 0),
            pady=(5, 15),
        )

        email_label = ctk.CTkLabel(
            fields_frame,
            text="E-mail remetente",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        email_label.grid(
            row=2,
            column=0,
            sticky="w",
        )

        password_label = ctk.CTkLabel(
            fields_frame,
            text="Senha SMTP",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        password_label.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(10, 0),
        )

        self.sender_entry = ctk.CTkEntry(
            fields_frame,
            height=42,
            font=("Segoe UI", 13),
        )

        self.sender_entry.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(5, 15),
        )

        self.password_entry = ctk.CTkEntry(
            fields_frame,
            height=42,
            font=("Segoe UI", 13),
            show="●",
        )

        self.password_entry.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=(10, 0),
            pady=(5, 15),
        )

        timeout_label = ctk.CTkLabel(
            fields_frame,
            text="Timeout (segundos)",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        timeout_label.grid(
            row=4,
            column=0,
            sticky="w",
        )

        self.timeout_entry = ctk.CTkEntry(
            fields_frame,
            height=42,
            font=("Segoe UI", 13),
        )

        self.timeout_entry.grid(
            row=5,
            column=0,
            sticky="ew",
            pady=(5, 20),
        )

        security_frame = ctk.CTkFrame(
            fields_frame,
            fg_color="transparent",
        )

        security_frame.grid(
            row=5,
            column=1,
            sticky="w",
            padx=(10, 0),
            pady=(5, 20),
        )

        self.tls_variable = ctk.BooleanVar(
            value=True
        )

        self.ssl_variable = ctk.BooleanVar(
            value=False
        )

        self.tls_switch = ctk.CTkSwitch(
            security_frame,
            text="TLS",
            variable=self.tls_variable,
            command=self._on_tls_changed,
        )

        self.tls_switch.pack(
            side="left",
            padx=(0, 20),
        )

        self.ssl_switch = ctk.CTkSwitch(
            security_frame,
            text="SSL",
            variable=self.ssl_variable,
            command=self._on_ssl_changed,
        )

        self.ssl_switch.pack(
            side="left",
        )

    def _create_save_area(self) -> None:
        """Cria botão e mensagem de status."""

        self.status_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        self.status_label.pack(
            anchor="w",
            pady=(0, 8),
        )

        self.save_button = ctk.CTkButton(
            self.content_frame,
            text="SALVAR CONFIGURAÇÕES",
            height=48,
            corner_radius=8,
            font=("Segoe UI", 13, "bold"),
            fg_color=ThemeColors.SECONDARY,
            hover_color="#692027",
            command=self._save_settings,
        )

        self.save_button.pack(
            fill="x",
            pady=(0, 20),
        )

    def refresh(self) -> None:
        """Recarrega os dados atuais do config.ini."""

        self._config_manager.reload()

        self._set_entry(
            self.store_entry,
            self._config_manager.store_name,
        )

        self._set_entry(
            self.smtp_server_entry,
            self._config_manager.smtp_server,
        )

        self._set_entry(
            self.smtp_port_entry,
            str(self._config_manager.smtp_port),
        )

        self._set_entry(
            self.sender_entry,
            self._config_manager.sender_email,
        )

        self._set_entry(
            self.password_entry,
            self._config_manager.password,
        )

        self._set_entry(
            self.timeout_entry,
            str(self._config_manager.timeout),
        )

        self.tls_variable.set(
            self._config_manager.use_tls
        )

        self.ssl_variable.set(
            self._config_manager.use_ssl
        )

        self.status_label.configure(
            text=""
        )

    @staticmethod
    def _set_entry(
        entry: ctk.CTkEntry,
        value: str,
    ) -> None:
        """Define o conteúdo de um campo."""

        entry.delete(
            0,
            "end",
        )

        entry.insert(
            0,
            value,
        )

    def _on_tls_changed(self) -> None:
        """Evita TLS e SSL ativos simultaneamente."""

        if self.tls_variable.get():
            self.ssl_variable.set(False)

    def _on_ssl_changed(self) -> None:
        """Evita SSL e TLS ativos simultaneamente."""

        if self.ssl_variable.get():
            self.tls_variable.set(False)

    def _validate_fields(self) -> bool:
            """Valida os campos antes de salvar."""

            store_name = (
                self.store_entry.get().strip()
            )

            smtp_server = (
                self.smtp_server_entry.get().strip()
            )

            sender_email = (
                self.sender_entry.get().strip()
            )

            smtp_port = (
                self.smtp_port_entry.get().strip()
            )

            timeout = (
                self.timeout_entry.get().strip()
            )

            use_tls = (
                self.tls_variable.get()
            )

            use_ssl = (
                self.ssl_variable.get()
            )

            if not Validators.is_valid_store_name(
                store_name
            ):
                self._show_error(
                    "Informe o nome da loja."
                )
                return False

            if not Validators.is_valid_smtp_server(
                smtp_server
            ):
                self._show_error(
                    "Informe o servidor SMTP."
                )
                return False

            if not Validators.is_valid_email(
                sender_email
            ):
                self._show_error(
                    "Informe um e-mail remetente válido."
                )
                return False

            if not Validators.is_valid_port(
                smtp_port
            ):
                self._show_error(
                    "Informe uma porta SMTP válida."
                )
                return False

            if not Validators.is_valid_timeout(
                timeout
            ):
                self._show_error(
                    "Informe um timeout válido."
                )
                return False

            if not Validators.is_valid_security_mode(
                use_tls,
                use_ssl,
            ):
                self._show_error(
                    "TLS e SSL não podem ficar "
                    "ativos simultaneamente."
                )
                return False

            return True

    def _save_settings(self) -> None:
        """Salva as configurações no config.ini."""

        if not self._validate_fields():
            return

        try:
            self._config_manager.set(
                "LOJA",
                "NOME_LOJA",
                self.store_entry.get().strip(),
            )

            self._config_manager.set(
                "EMAIL",
                "SMTP_SERVER",
                self.smtp_server_entry.get().strip(),
            )

            self._config_manager.set(
                "EMAIL",
                "SMTP_PORT",
                int(
                    self.smtp_port_entry
                    .get()
                    .strip()
                ),
            )

            self._config_manager.set(
                "EMAIL",
                "EMAIL_REMETENTE",
                self.sender_entry.get().strip(),
            )

            self._config_manager.set(
                "EMAIL",
                "SENHA",
                self.password_entry.get(),
            )

            self._config_manager.set(
                "EMAIL",
                "TLS",
                self.tls_variable.get(),
            )

            self._config_manager.set(
                "EMAIL",
                "SSL",
                self.ssl_variable.get(),
            )

            self._config_manager.set(
                "EMAIL",
                "TIMEOUT",
                int(
                    self.timeout_entry
                    .get()
                    .strip()
                ),
            )

            self._config_manager.save()

            self.status_label.configure(
                text="Configurações salvas com sucesso.",
                text_color=ThemeColors.SUCCESS,
            )

        except Exception as error:
            self._show_error(
                f"Erro ao salvar: {error}"
            )

    def _show_error(
        self,
        message: str,
    ) -> None:
        """Exibe mensagem de erro."""

        self.status_label.configure(
            text=message,
            text_color=ThemeColors.ERROR,
        )