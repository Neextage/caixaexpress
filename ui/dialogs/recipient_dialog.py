"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : recipient_dialog.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Janela utilizada para inclusão e edição
de destinatários.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from tkinter import messagebox

from core.validators import Validators


class RecipientDialog(ctk.CTkToplevel):
    """Janela de cadastro de destinatários."""

    GROUPS = [
        "Diretoria",
        "Financeiro",
        "Supervisores",
        "TI",
    ]

    def __init__(
        self,
        master,
        database,
        recipient=None,
        on_saved=None,
    ) -> None:

        super().__init__(master)

        self._database = database
        self._recipient = recipient
        self._editing = recipient is not None
        self._on_saved = on_saved

        self.title(
            "Editar Destinatário"
            if self._editing
            else "Novo Destinatário"
        )

        self.geometry(
            "470x520"
        )

        self.resizable(
            False,
            False,
        )

        self.transient(master)
        self.grab_set()
        self.update_idletasks()

        x = (
            self.winfo_screenwidth() // 2
            - 250
        )

        y = (
            self.winfo_screenheight() // 2
            - 260
        )

        self.geometry(
            f"500x560+{x}+{y}"
        )

        self.configure(
            fg_color=ThemeColors.BACKGROUND
        )

        self._create_interface()
        
        if self._editing:
           self._load_recipient()

    def _create_interface(self) -> None:
        """Cria a interface da janela."""

        title = ctk.CTkLabel(
            self,
            text=(
                "Editar Destinatário"
                if self._editing
                else"Novo Destinatário"
            ),
            font=("Segoe UI", 24, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(25, 20),
        )

        #
        # Nome
        #

        ctk.CTkLabel(
            self,
            text="Nome",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        ).pack(
            anchor="w",
            padx=30,
        )

        self.name_entry = ctk.CTkEntry(
            self,
            width=400,
            height=38,
        )

        self.name_entry.pack(
            padx=30,
            pady=(5, 18),
        )

        #
        # E-mail
        #

        ctk.CTkLabel(
            self,
            text="E-mail",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        ).pack(
            anchor="w",
            padx=30,
        )

        self.email_entry = ctk.CTkEntry(
            self,
            width=400,
            height=38,
        )

        self.email_entry.pack(
            padx=30,
            pady=(5, 18),
        )

        #
        # Grupo
        #

        ctk.CTkLabel(
            self,
            text="Grupo",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        ).pack(
            anchor="w",
            padx=30,
        )

        self.group_option = ctk.CTkOptionMenu(
            self,
            width=400,
            values=self.GROUPS,
        )

        self.group_option.pack(
            padx=30,
            pady=(5, 20),
        )

        #
        # Ativo
        #

        self.active_switch = ctk.CTkSwitch(
            self,
            text="Destinatário ativo",
        )

        self.active_switch.select()

        self.active_switch.pack(
            anchor="w",
            padx=30,
        )

        #
        # Botões
        #

        buttons = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        buttons.pack(
            fill="x",
            padx=30,
            pady=30,
        )

        cancel_button = ctk.CTkButton(
            buttons,
            text="Cancelar",
            width=120,
            fg_color="#777777",
            command=self.destroy,
        )

        cancel_button.pack(
            side="left",
        )
        delete_button = ctk.CTkButton(
            buttons,
            text="Excluir",
            width=120,
            fg_color="#C62828",
            hover_color="#9F1D1D",
            command=self._delete,
        )

        if self._editing:

            delete_button.pack(
                side="left",
                padx=(15, 0),
            )

        save_button = ctk.CTkButton(
            buttons,
            text="Salvar",
            width=120,
            fg_color=ThemeColors.PRIMARY,
            command=self._save,
        )

        save_button.pack(
            side="right",
        )
    def _load_recipient(
        self,
    ) -> None:
        """Carrega os dados do destinatário."""

        self.name_entry.insert(
            0,
            self._recipient["name"],
        )

        self.email_entry.insert(
            0,
            self._recipient["email"],
        )

        self.group_option.set(
            self._recipient["group_name"],
        )

        if self._recipient["active"]:

            self.active_switch.select()

        else:

            self.active_switch.deselect()
    def _delete(self) -> None:
        """Exclui o destinatário."""

        if not messagebox.askyesno(
            "Caixa Express",
            "Deseja realmente excluir este destinatário?",
        ):
            return

        try:

            self._database.delete_recipient(
                self._recipient["id"],
            )

            messagebox.showinfo(
                "Caixa Express",
                "Destinatário excluído com sucesso.",
            )

            if callable(
                self._on_saved
            ):
                self._on_saved()

            self.destroy()

        except Exception as error:

            messagebox.showerror(
                "Caixa Express",
                f"Erro ao excluir destinatário.\n\n{error}",
            )

    def _save(self) -> None:
        """Salva um novo destinatário."""

        name = (
            self.name_entry
            .get()
            .strip()
        )

        email = (
            self.email_entry
            .get()
            .strip()
            .lower()
        )

        group = (
            self.group_option.get()
            .strip()
        )

        active = (
            self.active_switch.get() == 1
        )

        if not name:

            messagebox.showwarning(
                "Caixa Express",
                "Informe o nome do destinatário.",
            )

            return

        if not Validators.is_valid_email(
            email
        ):

            messagebox.showwarning(
                "Caixa Express",
                "Informe um e-mail válido.",
            )

            return

        if self._editing:

            existing = self._database.fetch_one(
                """
                SELECT id
                FROM recipients
                WHERE LOWER(email)=LOWER(?)
                AND id<>?
                """,
                (
                    email,
                    self._recipient["id"],
                ),
            )

        else:

            existing = self._database.fetch_one(
                """
                SELECT id
                FROM recipients
                WHERE LOWER(email)=LOWER(?)
                """,
                (
                    email,
                ),
            )

        if existing:

            messagebox.showwarning(
                "Caixa Express",
                "Este e-mail já está cadastrado.",
            )

            return

        try:

            if self._editing:

                self._database.update_recipient(
                    recipient_id=self._recipient["id"],
                    group_name=group,
                    name=name,
                    email=email,
                    active=active,
                )

                messagebox.showinfo(
                    "Caixa Express",
                    "Destinatário atualizado com sucesso.",
                )

            else:

                self._database.add_recipient(
                    group_name=group,
                    name=name,
                    email=email,
                    active=active,
                )

                messagebox.showinfo(
                    "Caixa Express",
                    "Destinatário cadastrado com sucesso.",
                )

            if callable(
                self._on_saved
            ):
                self._on_saved()

            self.destroy()

        except Exception as error:

            messagebox.showerror(
                "Caixa Express",
                f"Erro ao cadastrar destinatário.\n\n{error}",
            )