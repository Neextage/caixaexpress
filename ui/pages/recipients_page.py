"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : recipients_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Página administrativa para visualização e controle
dos destinatários dos relatórios.
---------------------------------------------------------
"""

from __future__ import annotations

import tkinter as tk

import customtkinter as ctk

from config.theme import ThemeColors
from core.database import DatabaseManager
from ui.dialogs.recipient_dialog import RecipientDialog

class RecipientsPage(ctk.CTkFrame):
    """Página de gerenciamento dos destinatários."""

    def __init__(
        self,
        master,
        database: DatabaseManager,
    ) -> None:
        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._database = database

        self._recipient_widgets: list[
            ctk.CTkFrame
        ] = []

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria a estrutura da página."""

        header = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        header.pack(
            fill="x",
            padx=45,
            pady=(40, 20),
        )

        title_area = ctk.CTkFrame(
            header,
            fg_color="transparent",
        )

        title_area.pack(
            side="left",
        )

        title = ctk.CTkLabel(
            title_area,
            text="Destinatários",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
        )

        description = ctk.CTkLabel(
            title_area,
            text=(
                "Controle quem receberá os "
                "relatórios de fechamento."
            ),
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            pady=(4, 0),
        )

        buttons_frame = ctk.CTkFrame(
            header,
            fg_color="transparent",
        )

        buttons_frame.pack(
            side="right",
        )

        new_button = ctk.CTkButton(
            buttons_frame,
            text="+ Novo",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=ThemeColors.SUCCESS,
            hover_color="#1F8A46",
            command=self._new_recipient,
        )

        new_button.pack(
            side="left",
            padx=(0, 10),
        )

        refresh_button = ctk.CTkButton(
            buttons_frame,
            text="Atualizar",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=ThemeColors.PRIMARY,
            hover_color="#26356F",
            command=self.refresh,
        )

        refresh_button.pack(
            side="left",
        )

        self.summary_frame = ctk.CTkFrame(
            self,
            fg_color=ThemeColors.SURFACE,
            corner_radius=12,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        self.summary_frame.pack(
            fill="x",
            padx=45,
            pady=(0, 15),
        )

        self.total_label = ctk.CTkLabel(
            self.summary_frame,
            text="Total: 0",
            font=("Segoe UI", 13, "bold"),
            text_color=ThemeColors.TEXT,
        )

        self.total_label.pack(
            side="left",
            padx=20,
            pady=14,
        )

        self.active_label = ctk.CTkLabel(
            self.summary_frame,
            text="Ativos: 0",
            font=("Segoe UI", 13, "bold"),
            text_color=ThemeColors.SUCCESS,
        )

        self.active_label.pack(
            side="left",
            padx=20,
            pady=14,
        )

        self.inactive_label = ctk.CTkLabel(
            self.summary_frame,
            text="Inativos: 0",
            font=("Segoe UI", 13, "bold"),
            text_color=ThemeColors.ERROR,
        )

        self.inactive_label.pack(
            side="left",
            padx=20,
            pady=14,
        )

        self.list_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            corner_radius=0,
        )

        self.list_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=(0, 35),
        )

    def refresh(self) -> None:
        """Atualiza a listagem de destinatários."""

        self._clear_list()

        recipients = (
            self._database
            .get_all_recipients()
        )

        total = len(recipients)

        active_count = sum(
            1
            for recipient in recipients
            if recipient["active"]
        )

        inactive_count = (
            total - active_count
        )

        self.total_label.configure(
            text=f"Total: {total}"
        )

        self.active_label.configure(
            text=f"Ativos: {active_count}"
        )

        self.inactive_label.configure(
            text=f"Inativos: {inactive_count}"
        )

        if not recipients:
            self._create_empty_state()
            return

        current_group = None

        for recipient in recipients:

            group_name = recipient[
                "group_name"
            ]

            if group_name != current_group:
                current_group = group_name

                self._create_group_title(
                    group_name
                )

            self._create_recipient_card(
                recipient
            )

    def _clear_list(self) -> None:
        """Remove os elementos da listagem."""

        for widget in (
            self.list_frame.winfo_children()
        ):
            widget.destroy()

        self._recipient_widgets.clear()

    def _create_group_title(
        self,
        group_name: str,
    ) -> None:
        """Cria o título de um grupo."""

        label = ctk.CTkLabel(
            self.list_frame,
            text=group_name.upper(),
            font=("Segoe UI", 12, "bold"),
            text_color=ThemeColors.PRIMARY,
        )

        label.pack(
            fill="x",
            anchor="w",
            pady=(15, 7),
        )

    def _create_recipient_card(
        self,
        recipient,
    ) -> None:
        """Cria o cartão de um destinatário."""

        card = ctk.CTkFrame(
            self.list_frame,
            height=75,
            corner_radius=10,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.pack(
            fill="x",
            pady=4,
        )
        card.bind(
            "<Button-1>",
            lambda e,
            recipient=recipient:
                self._edit_recipient(
                    recipient
                ),
        )

        card.pack_propagate(
            False
        )

        information = ctk.CTkFrame(
            card,
            fg_color="transparent",
        )

        information.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=12,
        )

        name_label = ctk.CTkLabel(
            information,
            text=recipient["name"],
            font=("Segoe UI", 14, "bold"),
            text_color=ThemeColors.TEXT,
        )

        name_label.pack(
            anchor="w",
        )
        name_label.bind(
            "<Button-1>",
            lambda e,
            recipient=recipient:
                self._edit_recipient(
                    recipient
                ),
        )

        email_label = ctk.CTkLabel(
            information,
            text=recipient["email"],
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        email_label.pack(
            anchor="w",
            pady=(3, 0),
        )
        email_label.bind(
            "<Button-1>",
            lambda e,
            recipient=recipient:
                self._edit_recipient(
                    recipient
                ),
        )

        switch_variable = tk.BooleanVar(
            value=bool(
                recipient["active"]
            )
        )

        switch = ctk.CTkSwitch(
            card,
            text=(
                "Ativo"
                if recipient["active"]
                else "Inativo"
            ),
            variable=switch_variable,
            width=100,
            font=("Segoe UI", 12),
        )

        switch.configure(
            command=lambda: (
                self._toggle_recipient(
                    recipient["id"],
                    switch_variable,
                    switch,
                )
            )
        )

        switch.pack(
            side="right",
            padx=20,
        )

        self._recipient_widgets.append(
            card
        )

    def _toggle_recipient(
        self,
        recipient_id: int,
        variable: tk.BooleanVar,
        switch: ctk.CTkSwitch,
    ) -> None:
        """Ativa ou desativa um destinatário."""

        active = bool(
            variable.get()
        )

        try:
            self._database.set_recipient_active(
                recipient_id,
                active,
            )

            switch.configure(
                text=(
                    "Ativo"
                    if active
                    else "Inativo"
                )
            )

            self._update_summary()

        except Exception:
            variable.set(
                not active
            )

            switch.configure(
                text=(
                    "Ativo"
                    if not active
                    else "Inativo"
                )
            )

    def _update_summary(self) -> None:
        """Atualiza os indicadores da página."""

        recipients = (
            self._database
            .get_all_recipients()
        )

        total = len(
            recipients
        )

        active_count = sum(
            1
            for recipient in recipients
            if recipient["active"]
        )

        inactive_count = (
            total - active_count
        )

        self.total_label.configure(
            text=f"Total: {total}"
        )

        self.active_label.configure(
            text=f"Ativos: {active_count}"
        )

        self.inactive_label.configure(
            text=f"Inativos: {inactive_count}"
        )
    def _edit_recipient(
        self,
        recipient,
    ) -> None:
        """Abre a janela de edição."""

        RecipientDialog(
            master=self,
            database=self._database,
            recipient=recipient,
            on_saved=self.refresh,
        )
    def _new_recipient(self) -> None:
        """Abre a janela de cadastro."""

        RecipientDialog(
           master=self,
           database=self._database,
           recipient=None,
           on_saved=self.refresh,
        )

    def _create_empty_state(self) -> None:
        """Exibe mensagem quando não há registros."""

        message = ctk.CTkLabel(
            self.list_frame,
            text=(
                "Nenhum destinatário "
                "cadastrado."
            ),
            font=("Segoe UI", 14),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        message.pack(
            pady=50,
        )