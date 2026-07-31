"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : app.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Janela principal e controlador de navegação da aplicação.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from config.version import AppInfo
from core.config_manager import ConfigManager
from ui.components.sidebar import Sidebar
from ui.pages.history_page import HistoryPage
from ui.pages.home_page import HomePage
from ui.pages.logs_page import LogsPage
from ui.pages.recipients_page import RecipientsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.tests_page import TestsPage


class CaixaExpressApp(ctk.CTk):
    """Janela principal do Caixa Express."""

    WIDTH = 1200
    HEIGHT = 700

    def __init__(
        self,
        config_manager: ConfigManager,
    ) -> None:
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        super().__init__()

        self._config_manager = config_manager

        self._pages: dict[str, ctk.CTkFrame] = {}
        self._current_page: str | None = None

        self._configure_window()
        self._create_layout()
        self._create_pages()

        self.show_page("home")

    def _configure_window(self) -> None:
        """Configura a janela principal."""

        self.title(
            f"{AppInfo.NAME} - v{AppInfo.VERSION}"
        )

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}"
        )

        self.minsize(
            self.WIDTH,
            self.HEIGHT,
        )

        self._center_window()

    def _center_window(self) -> None:
        """Centraliza a janela no monitor."""

        self.update_idletasks()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - self.WIDTH) // 2
        y = (screen_height - self.HEIGHT) // 2

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}"
        )

    def _create_layout(self) -> None:
        """Cria a estrutura principal."""

        self.configure(
            fg_color=ThemeColors.BACKGROUND
        )

        self.grid_columnconfigure(
            0,
            weight=0,
        )

        self.grid_columnconfigure(
            1,
            weight=1,
        )

        self.grid_rowconfigure(
            0,
            weight=1,
        )

        self.sidebar = Sidebar(
            self,
            on_navigation=self.show_page,
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        self.content.grid_rowconfigure(
            0,
            weight=1,
        )

        self.content.grid_columnconfigure(
            0,
            weight=1,
        )

    def _create_pages(self) -> None:
        """Inicializa todas as páginas."""

        self._pages = {
            "home": HomePage(
                self.content,
                self._config_manager,
            ),
            "recipients": RecipientsPage(
                self.content
            ),
            "settings": SettingsPage(
                self.content
            ),
            "history": HistoryPage(
                self.content
            ),
            "logs": LogsPage(
                self.content
            ),
            "tests": TestsPage(
                self.content
            ),
        }

        for page in self._pages.values():
            page.grid(
                row=0,
                column=0,
                sticky="nsew",
            )

    def show_page(
        self,
        page_name: str,
    ) -> None:
        """Exibe a página solicitada."""

        page = self._pages.get(page_name)

        if page is None:
            return

        page.tkraise()

        self._current_page = page_name

        self.sidebar.set_active(
            page_name
        )

    def run(self) -> None:
        """Inicia o loop gráfico."""

        self.mainloop()