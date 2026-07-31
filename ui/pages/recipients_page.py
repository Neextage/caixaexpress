"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : recipients_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
"""

import customtkinter as ctk

from config.theme import ThemeColors


class RecipientsPage(ctk.CTkFrame):

    def __init__(self, master) -> None:
        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        label = ctk.CTkLabel(
            self,
            text="Destinatários",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )
        label.pack(
            anchor="w",
            padx=45,
            pady=45,
        )