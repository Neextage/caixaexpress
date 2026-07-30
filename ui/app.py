"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : app.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Janela principal da aplicação.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.version import AppInfo


class CaixaExpressApp(ctk.CTk):
    """Janela principal da aplicação."""

    WIDTH = 1200
    HEIGHT = 700

    def __init__(self) -> None:
        super().__init__()

        self._configure_theme()
        self._configure_window()
        self._create_layout()

    def _configure_theme(self) -> None:
        """Configura o tema da aplicação."""

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    def _configure_window(self) -> None:
        """Configura a janela principal."""

        self.title(f"{AppInfo.NAME} - v{AppInfo.VERSION}")

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.minsize(self.WIDTH, self.HEIGHT)
        self.maxsize(self.WIDTH, self.HEIGHT)

        self._center_window()

    def _center_window(self) -> None:
        """Centraliza a janela na tela."""

        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - self.WIDTH) / 2)
        y = int((screen_height - self.HEIGHT) / 2)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

    def _create_layout(self) -> None:
        """Cria a estrutura inicial da interface."""

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="Caixa Express",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            pady=(30, 10)
        )

        version = ctk.CTkLabel(
            self.sidebar,
            text=f"Versão {AppInfo.VERSION}"
        )

        version.pack()

        placeholder = ctk.CTkLabel(
            self.content,
            text="Bem-vindo ao Caixa Express",
            font=("Segoe UI", 28, "bold")
        )

        placeholder.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def run(self) -> None:
        """Inicia a aplicação."""

        self.mainloop()