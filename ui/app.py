"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : app.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Janela principal, navegação e controle de acesso
administrativo do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from config.version import AppInfo
from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.logger_manager import LoggerManager
from ui.components.sidebar import Sidebar
from ui.login_dialog import LoginDialog
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

    ADMIN_PAGES = {
        "recipients",
        "settings",
        "history",
        "logs",
        "tests",
    }

    def __init__(
        self,
        config_manager: ConfigManager,
        database: DatabaseManager,
        logger: LoggerManager,
    ) -> None:

        ctk.set_appearance_mode(
            "light"
        )

        ctk.set_default_color_theme(
            "blue"
        )

        super().__init__()

        self._config_manager = (
            config_manager
        )

        self._database = database
        self._logger = logger

        self._pages: dict[
            str,
            ctk.CTkFrame,
        ] = {}

        self._current_page: (
            str | None
        ) = None

        self._admin_authenticated = False

        self._login_dialog: (
            LoginDialog | None
        ) = None

        self._configure_window()
        self._create_layout()
        self._create_pages()

        self._open_page(
            "home"
        )

    def _configure_window(self) -> None:
        """Configura a janela principal."""

        self.title(
            f"{AppInfo.NAME} - "
            f"v{AppInfo.VERSION}"
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
            f"{self.WIDTH}x{self.HEIGHT}"
            f"+{x}+{y}"
        )

    def _create_layout(self) -> None:
        """Cria o layout principal."""

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
        """Cria as páginas."""

        self._pages = {

            "home": HomePage(
                self.content,
                self._config_manager,
            ),

            "recipients": RecipientsPage(
                self.content,
                self._database,
            ),

            "settings": SettingsPage(
                self.content,
                self._config_manager,
            ),

            "history": HistoryPage(
                self.content,
                self._database,
            ),

            "logs": LogsPage(
                self.content,
                self._logger,
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
        """Solicita navegação para uma página."""

        if (
            page_name in self.ADMIN_PAGES
            and not self._admin_authenticated
        ):

            self.sidebar.set_active(
                self._current_page
                or "home"
            )

            self._request_admin_access(
                page_name
            )

            return

        self._open_page(
            page_name
        )

    def _request_admin_access(
        self,
        page_name: str,
    ) -> None:
        """Solicita autenticação administrativa."""

        if (
            self._login_dialog is not None
            and
            self._login_dialog.winfo_exists()
        ):

            self._login_dialog.focus_force()

            return

        self._login_dialog = LoginDialog(
            self,
            self._config_manager,
            on_success=lambda: (
                self._admin_login_success(
                    page_name
                )
            ),
        )

    def _admin_login_success(
        self,
        page_name: str,
    ) -> None:
        """Libera a sessão administrativa."""

        self._admin_authenticated = True

        self._login_dialog = None

        self._open_page(
            page_name
        )

    def _open_page(
        self,
        page_name: str,
    ) -> None:
        """Abre efetivamente uma página."""

        page = self._pages.get(
            page_name
        )

        if page is None:
            return

        if hasattr(
            page,
            "refresh",
        ):
            page.refresh()

        page.tkraise()

        self._current_page = page_name

        self.sidebar.set_active(
            page_name
        )

    def run(self) -> None:
        """Inicia a aplicação."""

        self.mainloop()