"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : about_dialog.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 1.0.0
---------------------------------------------------------
Descrição:
Janela "Sobre" do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import os
import webbrowser

import customtkinter as ctk
from PIL import Image

from config.theme import ThemeColors
from config.version import AppInfo


class AboutDialog(ctk.CTkToplevel):
    """Janela Sobre."""

    WIDTH = 560
    HEIGHT = 640

    def __init__(
        self,
        master,
    ) -> None:

        super().__init__(master)

        self.title(
            "Sobre"
        )

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}"
        )

        self.resizable(
            False,
            False,
        )

        self.transient(master)
        self.grab_set()

        self.configure(
            fg_color=ThemeColors.BACKGROUND
        )

        self._center_window()

        self._create_interface()

    def _center_window(self) -> None:
        """Centraliza a janela."""

        self.update_idletasks()

        screen_width = (
            self.winfo_screenwidth()
        )

        screen_height = (
            self.winfo_screenheight()
        )

        x = (
            screen_width
            - self.WIDTH
        ) // 2

        y = (
            screen_height
            - self.HEIGHT
        ) // 2

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}"
        )

    def _create_interface(
        self,
    ) -> None:
        """Cria a interface."""

        container = ctk.CTkFrame(
            self,
            fg_color=ThemeColors.BACKGROUND,
            corner_radius=0,
        )

        container.pack(
            fill="both",
            expand=True,
        )

        #
        # Ícone
        #

        icon_path = os.path.join(
            "assets",
            "icon.png",
        )

        if os.path.exists(
            icon_path
        ):

            image = ctk.CTkImage(
                light_image=Image.open(
                    icon_path
                ),
                dark_image=Image.open(
                    icon_path
                ),
                size=(110, 110),
            )

            icon = ctk.CTkLabel(
                container,
                image=image,
                text="",
            )

            icon.pack(
                pady=(35, 20),
            )

        #
        # Nome
        #

        title = ctk.CTkLabel(
            container,
            text="CAIXA EXPRESS",
            font=(
                "Segoe UI",
                30,
                "bold",
            ),
            text_color=ThemeColors.PRIMARY,
        )

        title.pack()

        #
        # Descrição
        #

        subtitle = ctk.CTkLabel(
            container,
            text=(
                "Sistema de Envio de "
                "Fechamento de Caixa"
            ),
            font=(
                "Segoe UI",
                15,
            ),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        subtitle.pack(
            pady=(6, 18),
        )

        #
        # Versão
        #

        version = ctk.CTkLabel(
            container,
            text=(
                f"Versão {AppInfo.VERSION}"
            ),
            font=(
                "Segoe UI",
                14,
                "bold",
            ),
            text_color=ThemeColors.SUCCESS,
        )

        version.pack()

        #
        # Desenvolvedor
        #

        author = ctk.CTkLabel(
            container,
            text=(
                "Desenvolvido por\n\n"
                "Dylan Ryan Pereira Santos"
            ),
            justify="center",
            font=(
                "Segoe UI",
                14,
            ),
            text_color=ThemeColors.TEXT,
        )

        author.pack(
            pady=(20, 25),
        )

        #
        # Tecnologias
        #

        technologies_title = ctk.CTkLabel(
            container,
            text="Tecnologias",
            font=(
                "Segoe UI",
                18,
                "bold",
            ),
            text_color=ThemeColors.PRIMARY,
        )

        technologies_title.pack()
        technologies = ctk.CTkLabel(
            container,
            text=(
                "• Python 3.14\n"
                "• CustomTkinter\n"
                "• SQLite\n"
                "• SMTP\n"
                "• HTML\n"
                "• Git\n"
                "• GitHub"
            ),
            justify="center",
            font=(
                "Segoe UI",
                14,
            ),
            text_color=ThemeColors.TEXT,
        )

        technologies.pack(
            pady=(8, 25),
        )

        #
        # Informações
        #

        info = ctk.CTkLabel(
            container,
            text=(
                "Software desenvolvido para automatizar\n"
                "o envio do fechamento diário de caixa."
            ),
            justify="center",
            font=(
                "Segoe UI",
                13,
            ),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        info.pack()

        #
        # Copyright
        #

        copyright_label = ctk.CTkLabel(
            container,
            text=(
                "© 2026 Dylan Ryan Pereira Santos\n"
                "Todos os direitos reservados."
            ),
            justify="center",
            font=(
                "Segoe UI",
                12,
            ),
            text_color="#888888",
        )

        copyright_label.pack(
            pady=(25, 30),
        )

        #
        # Botões
        #

        buttons = ctk.CTkFrame(
            container,
            fg_color="transparent",
        )

        buttons.pack(
            pady=(0, 20),
        )

        github_button = ctk.CTkButton(
            buttons,
            text="GitHub",
            width=140,
            height=40,
            fg_color=ThemeColors.PRIMARY,
            hover_color="#26356F",
            command=self._open_github,
        )

        github_button.pack(
            side="left",
            padx=(0, 10),
        )

        close_button = ctk.CTkButton(
            buttons,
            text="Fechar",
            width=140,
            height=40,
            fg_color="#666666",
            hover_color="#4F4F4F",
            command=self.destroy,
        )

        close_button.pack(
            side="left",
        )

    def _open_github(
        self,
    ) -> None:
        """Abre o repositório do projeto."""

        webbrowser.open(
            "https://github.com/Neextage/caixaexpress"
        )