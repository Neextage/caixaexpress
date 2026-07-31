"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : login_dialog.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Janela de autenticação para acesso às áreas
administrativas do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from config.theme import ThemeColors
from core.auth_manager import AuthManager
from core.config_manager import ConfigManager


class LoginDialog(ctk.CTkToplevel):
    """Janela de autenticação administrativa."""

    WIDTH = 430
    HEIGHT = 300

    def __init__(
        self,
        master,
        config_manager: ConfigManager,
        on_success: Callable[[], None],
    ) -> None:
        super().__init__(master)

        self._config_manager = config_manager
        self._on_success = on_success

        self._configure_window()
        self._create_interface()

        self.after(
            100,
            self._prepare_dialog,
        )

    def _configure_window(self) -> None:
        """Configura a janela."""

        self.title(
            "Acesso Administrativo"
        )

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}"
        )

        self.resizable(
            False,
            False,
        )

        self.configure(
            fg_color=ThemeColors.BACKGROUND,
        )

        self.protocol(
            "WM_DELETE_WINDOW",
            self._cancel,
        )

        self._center_window()

    def _center_window(self) -> None:
        """Centraliza em relação à janela principal."""

        self.update_idletasks()

        master_x = self.master.winfo_x()
        master_y = self.master.winfo_y()

        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()

        x = (
            master_x
            + (master_width - self.WIDTH) // 2
        )

        y = (
            master_y
            + (master_height - self.HEIGHT) // 2
        )

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}"
        )

    def _create_interface(self) -> None:
        """Cria os componentes visuais."""

        title = ctk.CTkLabel(
            self,
            text="Acesso Administrativo",
            font=("Segoe UI", 22, "bold"),
            text_color=ThemeColors.TEXT,
        )
        title.pack(
            pady=(30, 5),
        )

        description = ctk.CTkLabel(
            self,
            text=(
                "Informe a senha para acessar "
                "esta área."
            ),
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )
        description.pack(
            pady=(0, 20),
        )

        self.password_entry = ctk.CTkEntry(
            self,
            width=340,
            height=44,
            placeholder_text="Senha administrativa",
            show="●",
            font=("Segoe UI", 14),
        )
        self.password_entry.pack()

        self.password_entry.bind(
            "<Return>",
            self._authenticate_event,
        )

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 12),
            text_color=ThemeColors.ERROR,
        )
        self.error_label.pack(
            pady=(7, 3),
        )

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        buttons.pack(
            pady=(5, 0),
        )

        cancel_button = ctk.CTkButton(
            buttons,
            text="Cancelar",
            width=150,
            height=42,
            fg_color="#6B7280",
            hover_color="#4B5563",
            command=self._cancel,
        )
        cancel_button.grid(
            row=0,
            column=0,
            padx=5,
        )

        login_button = ctk.CTkButton(
            buttons,
            text="Entrar",
            width=150,
            height=42,
            fg_color=ThemeColors.SECONDARY,
            hover_color="#692027",
            command=self._authenticate,
        )
        login_button.grid(
            row=0,
            column=1,
            padx=5,
        )

    def _prepare_dialog(self) -> None:
        """Ativa comportamento modal."""

        self.transient(
            self.master
        )

        self.grab_set()

        self.password_entry.focus_set()

    def _authenticate_event(
        self,
        _event=None,
    ) -> None:
        """Permite autenticar pressionando Enter."""

        self._authenticate()

    def _authenticate(self) -> None:
        """Valida a senha informada."""

        password = self.password_entry.get()

        stored_hash = (
            self._config_manager
            .admin_password_hash
        )

        if not stored_hash:
            self.error_label.configure(
                text=(
                    "Senha administrativa "
                    "não configurada."
                )
            )
            return

        valid = AuthManager.verify_password(
            password,
            stored_hash,
        )

        if not valid:
            self.password_entry.delete(
                0,
                "end",
            )

            self.error_label.configure(
                text="Senha incorreta."
            )

            self.password_entry.focus_set()

            return

        self.grab_release()
        self.destroy()

        self._on_success()

    def _cancel(self) -> None:
        """Cancela a autenticação."""

        try:
            self.grab_release()
        except Exception:
            pass

        self.destroy()