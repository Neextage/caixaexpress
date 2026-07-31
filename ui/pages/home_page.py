"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : home_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Tela pública utilizada pelas lojas para informar o valor
do fechamento de caixa e realizar o envio do relatório.
---------------------------------------------------------
"""

from __future__ import annotations

import re
import uuid
from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk

from config.theme import ThemeColors
from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.email_sender import EmailSender


class HomePage(ctk.CTkFrame):
    """Tela pública de fechamento de caixa."""

    def __init__(
        self,
        master,
        config_manager: ConfigManager,
        database: DatabaseManager,
        email_sender: EmailSender,
    ) -> None:

        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._config_manager = config_manager
        self._database = database
        self._email_sender = email_sender

        self._editing_value = False
        self._sending = False

        self._create_interface()
        self._load_store()
        self._configure_currency_entry()

    def _create_interface(self) -> None:
        """Cria a interface da página."""

        title = ctk.CTkLabel(
            self,
            text="Fechamento de Caixa",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=45,
            pady=(45, 5),
        )

        description = ctk.CTkLabel(
            self,
            text=(
                "Informe o valor total do caixa "
                "para realizar o envio."
            ),
            font=("Segoe UI", 14),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            padx=45,
            pady=(0, 30),
        )

        self.card = ctk.CTkFrame(
            self,
            width=620,
            height=365,
            corner_radius=16,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        self.card.pack(
            padx=45,
            anchor="w",
        )

        self.card.pack_propagate(
            False
        )

        store_title = ctk.CTkLabel(
            self.card,
            text="Loja",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        store_title.pack(
            anchor="w",
            padx=35,
            pady=(35, 5),
        )

        self.store_label = ctk.CTkLabel(
            self.card,
            text="CARREGANDO...",
            font=("Segoe UI", 21, "bold"),
            text_color=ThemeColors.PRIMARY,
        )

        self.store_label.pack(
            anchor="w",
            padx=35,
        )

        value_title = ctk.CTkLabel(
            self.card,
            text="Valor do Caixa",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        value_title.pack(
            anchor="w",
            padx=35,
            pady=(30, 7),
        )

        self.value_variable = ctk.StringVar(
            value="R$ 0,00"
        )

        self.value_entry = ctk.CTkEntry(
            self.card,
            width=550,
            height=55,
            textvariable=self.value_variable,
            font=("Segoe UI", 20, "bold"),
            corner_radius=8,
            border_width=1,
            border_color=ThemeColors.BORDER,
            text_color=ThemeColors.TEXT,
            justify="left",
        )

        self.value_entry.pack(
            padx=35,
        )

        self.send_button = ctk.CTkButton(
            self.card,
            text="ENVIAR RELATÓRIO",
            width=550,
            height=52,
            corner_radius=8,
            font=("Segoe UI", 14, "bold"),
            fg_color=ThemeColors.SECONDARY,
            hover_color="#692027",
            command=self._send_report,
        )

        self.send_button.pack(
            padx=35,
            pady=(30, 0),
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="Sistema pronto.",
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        self.status_label.pack(
            anchor="w",
            padx=45,
            pady=20,
        )

    def refresh(self) -> None:
        """Atualiza as informações exibidas na página."""

        self._config_manager.reload()
        self._load_store()

    def _load_store(self) -> None:
        """Carrega o nome da loja configurada."""

        store_name = (
            self._config_manager.store_name
        )

        if not store_name:

            self.store_label.configure(
                text="LOJA NÃO CONFIGURADA",
                text_color=ThemeColors.ERROR,
            )

            self.status_label.configure(
                text=(
                    "A loja precisa ser configurada "
                    "antes do envio."
                ),
                text_color=ThemeColors.ERROR,
            )

            self.send_button.configure(
                state="disabled"
            )

            return

        self.store_label.configure(
            text=store_name.upper(),
            text_color=ThemeColors.PRIMARY,
        )

        if not self._sending:
            self.send_button.configure(
                state="normal"
            )

    def _configure_currency_entry(self) -> None:
        """Configura a máscara monetária."""

        self.value_variable.trace_add(
            "write",
            self._on_value_changed,
        )

        self.value_entry.bind(
            "<FocusIn>",
            self._select_currency_value,
        )

    def _on_value_changed(
        self,
        *_args,
    ) -> None:
        """Formata o conteúdo digitado como moeda."""

        if self._editing_value:
            return

        self._editing_value = True

        try:

            current_value = (
                self.value_variable.get()
            )

            digits = re.sub(
                r"\D",
                "",
                current_value,
            )

            if not digits:
                digits = "0"

            cents = int(
                digits
            )

            formatted = (
                self._format_currency(
                    cents
                )
            )

            self.value_variable.set(
                formatted
            )

            self.value_entry.icursor(
                "end"
            )

        finally:
            self._editing_value = False

    @staticmethod
    def _format_currency(
        cents: int,
    ) -> str:
        """Converte centavos para moeda brasileira."""

        reais = cents // 100
        centavos = cents % 100

        reais_formatted = (
            f"{reais:,}"
            .replace(",", ".")
        )

        return (
            f"R$ {reais_formatted},"
            f"{centavos:02d}"
        )

    def _select_currency_value(
        self,
        _event=None,
    ) -> None:
        """Posiciona o cursor no final do valor."""

        self.after(
            10,
            lambda: (
                self.value_entry.icursor(
                    "end"
                )
            ),
        )

    def get_cash_value_cents(self) -> int:
        """Retorna o valor informado em centavos."""

        value = (
            self.value_variable.get()
        )

        digits = re.sub(
            r"\D",
            "",
            value,
        )

        if not digits:
            return 0

        return int(
            digits
        )

    def get_cash_value(self) -> float:
        """Retorna o valor informado em reais."""

        return (
            self.get_cash_value_cents()
            / 100
        )

    def clear_cash_value(self) -> None:
        """Limpa o valor do fechamento."""

        self.value_variable.set(
            "R$ 0,00"
        )

    def _send_report(self) -> None:
        """Executa o envio real do fechamento."""

        if self._sending:
            return

        store_name = (
            self._config_manager.store_name
            .strip()
        )

        cash_value = (
            self.get_cash_value()
        )

        if not store_name:

            self._show_error(
                "A loja não está configurada."
            )

            return

        if cash_value <= 0:

            self.status_label.configure(
                text=(
                    "Informe um valor de caixa "
                    "maior que R$ 0,00."
                ),
                text_color=ThemeColors.ERROR,
            )

            return

        recipients_rows = (
            self._database
            .get_active_recipients()
        )

        recipients = [
            row["email"]
            for row in recipients_rows
            if row["email"]
        ]

        if not recipients:

            self._show_error(
                "Nenhum destinatário ativo "
                "foi encontrado."
            )

            return

        protocol = (
            self._generate_protocol()
        )

        self._sending = True

        self.send_button.configure(
            state="disabled",
            text="ENVIANDO...",
        )

        self.status_label.configure(
            text="Enviando fechamento...",
            text_color=ThemeColors.TEXT_LIGHT,
        )

        self.update_idletasks()

        success, message = (
            self._email_sender
            .send_cash_report(
                store_name=store_name,
                cash_value=cash_value,
                recipients=recipients,
            )
        )

        now = datetime.now()

        status = (
            "SUCESSO"
            if success
            else "ERRO"
        )

        try:

            self._database.add_history(
                protocol=protocol,
                store_name=store_name,
                cash_value=cash_value,
                send_date=now.strftime(
                    "%d/%m/%Y"
                ),
                send_time=now.strftime(
                    "%H:%M:%S"
                ),
                status=status,
                message=message,
            )

        except Exception:
            pass

        self._sending = False

        self.send_button.configure(
            state="normal",
            text="ENVIAR RELATÓRIO",
        )

        if success:

            self.clear_cash_value()

            self.status_label.configure(
                text=(
                    "Caixa enviado com sucesso."
                ),
                text_color=ThemeColors.SUCCESS,
            )

            messagebox.showinfo(
                "Caixa Express",
                (
                    "Caixa enviado com sucesso.\n\n"
                    f"Protocolo: {protocol}"
                ),
                parent=self,
            )

            return

        self.status_label.configure(
            text="Falha no envio do fechamento.",
            text_color=ThemeColors.ERROR,
        )

        self._show_error(
            message
        )

    def _show_error(
        self,
        message: str,
    ) -> None:
        """Exibe uma mensagem de erro ao usuário."""

        messagebox.showerror(
            "Caixa Express - Erro",
            (
                f"{message}\n\n"
                "Por favor, entre em contato "
                "com Dylan ou Fabiano."
            ),
            parent=self,
        )

    @staticmethod
    def _generate_protocol() -> str:
        """Gera um protocolo único para o envio."""

        now = datetime.now()

        random_code = (
            uuid.uuid4()
            .hex[:6]
            .upper()
        )

        return (
            "CX-"
            f"{now:%Y%m%d-%H%M%S}-"
            f"{random_code}"
        )