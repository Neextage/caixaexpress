"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : home_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Tela pública de fechamento de caixa.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors


class HomePage(ctk.CTkFrame):
    """Tela principal do Caixa Express."""

    def __init__(self, master) -> None:
        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria os elementos da página."""

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
            text="Informe o valor total do caixa para realizar o envio.",
            font=("Segoe UI", 14),
            text_color=ThemeColors.TEXT_LIGHT,
        )
        description.pack(
            anchor="w",
            padx=45,
            pady=(0, 30),
        )

        card = ctk.CTkFrame(
            self,
            width=620,
            height=360,
            corner_radius=16,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )
        card.pack(
            padx=45,
            anchor="w",
        )
        card.pack_propagate(False)

        store_title = ctk.CTkLabel(
            card,
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
            card,
            text="NÃO CONFIGURADA",
            font=("Segoe UI", 21, "bold"),
            text_color=ThemeColors.PRIMARY,
        )
        self.store_label.pack(
            anchor="w",
            padx=35,
        )

        value_title = ctk.CTkLabel(
            card,
            text="Valor do Caixa",
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )
        value_title.pack(
            anchor="w",
            padx=35,
            pady=(30, 7),
        )

        self.value_entry = ctk.CTkEntry(
            card,
            width=550,
            height=52,
            placeholder_text="R$ 0,00",
            font=("Segoe UI", 18),
            corner_radius=8,
            border_color=ThemeColors.BORDER,
        )
        self.value_entry.pack(
            padx=35,
        )

        self.send_button = ctk.CTkButton(
            card,
            text="ENVIAR RELATÓRIO",
            width=550,
            height=50,
            corner_radius=8,
            font=("Segoe UI", 14, "bold"),
            fg_color=ThemeColors.SECONDARY,
            hover_color="#692027",
            command=self._send_placeholder,
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

    def _send_placeholder(self) -> None:
        """Ação temporária até a implementação do envio."""

        self.status_label.configure(
            text="O envio será habilitado na Sprint de SMTP."
        )