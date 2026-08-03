"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : sidebar.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 1.0.0
---------------------------------------------------------
Descrição:
Menu lateral principal da aplicação.
---------------------------------------------------------
"""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from config.theme import ThemeColors
from config.version import AppInfo
from ui.dialogs.about_dialog import AboutDialog


class Sidebar(ctk.CTkFrame):
    """Menu lateral utilizado na janela principal."""

    WIDTH = 230

    def __init__(
        self,
        master,
        on_navigation: Callable[[str], None],
    ) -> None:

        super().__init__(
            master,
            width=self.WIDTH,
            corner_radius=0,
            fg_color=ThemeColors.PRIMARY,
        )

        self._on_navigation = on_navigation
        self._buttons: dict[
            str,
            ctk.CTkButton,
        ] = {}

        self._active_page = "home"

        self.grid_propagate(
            False
        )

        self._create_header()
        self._create_menu()
        self._create_version()

        self.set_active(
            "home"
        )

    def _create_header(
        self,
    ) -> None:
        """Cria o cabeçalho do menu."""

        title = ctk.CTkLabel(
            self,
            text="CAIXA EXPRESS",
            font=(
                "Segoe UI",
                21,
                "bold",
            ),
            text_color="#FFFFFF",
        )

        title.pack(
            padx=20,
            pady=(32, 4),
            anchor="w",
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Fechamento de Caixa",
            font=(
                "Segoe UI",
                12,
            ),
            text_color="#B8BED7",
        )

        subtitle.pack(
            padx=20,
            pady=(0, 28),
            anchor="w",
        )

    def _create_menu(
        self,
    ) -> None:
        """Cria os botões do menu."""

        menu_items = [

            ("home", "Caixa"),

            ("recipients", "Destinatários"),

            ("settings", "Configuração"),

            ("history", "Histórico"),

            ("logs", "Logs"),

            ("tests", "Testes"),

            ("about", "Sobre"),
        ]

        for page_name, text in menu_items:

            button = ctk.CTkButton(

                self,

                text=text,

                height=46,

                corner_radius=8,

                anchor="w",

                font=(
                    "Segoe UI",
                    14,
                    "bold",
                ),

                fg_color="transparent",

                hover_color="#26356F",

                text_color="#FFFFFF",

                command=lambda page=page_name:
                self._navigate(page),
            )

            button.pack(

                fill="x",

                padx=14,

                pady=4,

            )

            self._buttons[
                page_name
            ] = button

    def _create_version(
        self,
    ) -> None:
        """Mostra a versão."""

        version_label = ctk.CTkLabel(

            self,

            text=(
                f"Versão {AppInfo.VERSION}"
            ),

            font=(
                "Segoe UI",
                11,
            ),

            text_color="#AEB5D0",

        )

        version_label.pack(

            side="bottom",

            padx=20,

            pady=22,

            anchor="w",

        )

    def _navigate(
        self,
        page_name: str,
    ) -> None:
        """Realiza a navegação."""

        if page_name == "about":

            AboutDialog(
                self.master,
            )

            return

        self.set_active(
            page_name
        )

        self._on_navigation(
            page_name
        )

    def set_active(
        self,
        page_name: str,
    ) -> None:
        """Destaca visualmente o botão ativo."""

        self._active_page = page_name

        for name, button in self._buttons.items():

            if name == page_name:

                button.configure(

                    fg_color=ThemeColors.SECONDARY,

                )

            else:

                button.configure(

                    fg_color="transparent",

                )