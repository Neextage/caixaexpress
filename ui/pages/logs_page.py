"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : logs_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Página administrativa para visualização dos logs
gerados pelo Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from core.logger_manager import LoggerManager


class LogsPage(ctk.CTkFrame):
    """Página de visualização dos logs."""

    def __init__(
        self,
        master,
        logger: LoggerManager,
    ) -> None:

        super().__init__(
            master,
            corner_radius=0,
            fg_color=ThemeColors.BACKGROUND,
        )

        self._logger = logger

        self._selected_level = ctk.StringVar(
            value="TODOS"
        )

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria a interface da página."""

        self._create_header()
        self._create_summary()
        self._create_filters()
        self._create_log_area()

    def _create_header(self) -> None:
        """Cria o cabeçalho."""

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
            text="Logs",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
        )

        description = ctk.CTkLabel(
            title_area,
            text=(
                "Acompanhe os eventos e erros "
                "registrados pelo Caixa Express."
            ),
            font=("Segoe UI", 13),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        description.pack(
            anchor="w",
            pady=(4, 0),
        )

        refresh_button = ctk.CTkButton(
            header,
            text="Atualizar",
            width=110,
            height=38,
            corner_radius=8,
            fg_color=ThemeColors.PRIMARY,
            hover_color="#26356F",
            command=self.refresh,
        )

        refresh_button.pack(
            side="right",
            pady=5,
        )

    def _create_summary(self) -> None:
        """Cria os indicadores."""

        summary = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        summary.pack(
            fill="x",
            padx=45,
            pady=(0, 15),
        )

        summary.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1,
        )

        self.total_value = (
            self._create_summary_card(
                summary,
                0,
                "Total",
                ThemeColors.PRIMARY,
            )
        )

        self.info_value = (
            self._create_summary_card(
                summary,
                1,
                "Informações",
                ThemeColors.PRIMARY,
            )
        )

        self.warning_value = (
            self._create_summary_card(
                summary,
                2,
                "Avisos",
                "#D97706",
            )
        )

        self.error_value = (
            self._create_summary_card(
                summary,
                3,
                "Erros",
                ThemeColors.ERROR,
            )
        )

    def _create_summary_card(
        self,
        master,
        column: int,
        title: str,
        value_color: str,
    ) -> ctk.CTkLabel:
        """Cria um card de indicador."""

        card = ctk.CTkFrame(
            master,
            height=82,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=5,
        )

        card.grid_propagate(
            False
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 11),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        title_label.pack(
            anchor="w",
            padx=16,
            pady=(12, 0),
        )

        value_label = ctk.CTkLabel(
            card,
            text="0",
            font=("Segoe UI", 21, "bold"),
            text_color=value_color,
        )

        value_label.pack(
            anchor="w",
            padx=16,
        )

        return value_label

    def _create_filters(self) -> None:
        """Cria os filtros da página."""

        filters = ctk.CTkFrame(
            self,
            corner_radius=10,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        filters.pack(
            fill="x",
            padx=45,
            pady=(0, 12),
        )

        label = ctk.CTkLabel(
            filters,
            text="Exibir:",
            font=("Segoe UI", 12, "bold"),
            text_color=ThemeColors.TEXT,
        )

        label.pack(
            side="left",
            padx=(18, 10),
            pady=12,
        )

        self.level_menu = ctk.CTkOptionMenu(
            filters,
            values=[
                "TODOS",
                "INFO",
                "WARNING",
                "ERROR",
            ],
            variable=self._selected_level,
            width=150,
            command=self._on_filter_changed,
        )

        self.level_menu.pack(
            side="left",
            pady=10,
        )

        self.visible_count_label = ctk.CTkLabel(
            filters,
            text="0 registros exibidos",
            font=("Segoe UI", 11),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        self.visible_count_label.pack(
            side="right",
            padx=18,
        )

    def _create_log_area(self) -> None:
        """Cria a área de visualização."""

        container = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        container.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=(0, 30),
        )

        self.log_textbox = ctk.CTkTextbox(
            container,
            corner_radius=8,
            border_width=0,
            font=(
                "Consolas",
                11,
            ),
            wrap="word",
        )

        self.log_textbox.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=12,
        )

        self.log_textbox.configure(
            state="disabled"
        )

    def refresh(self) -> None:
        """Atualiza os logs exibidos."""

        level = (
            self._selected_level.get()
        )

        logs = self._logger.read_logs(
            level=level,
            limit=500,
        )

        counts = (
            self._logger.get_log_counts()
        )

        self.total_value.configure(
            text=str(
                counts["total"]
            )
        )

        self.info_value.configure(
            text=str(
                counts["info"]
            )
        )

        self.warning_value.configure(
            text=str(
                counts["warning"]
            )
        )

        self.error_value.configure(
            text=str(
                counts["error"]
            )
        )

        self.visible_count_label.configure(
            text=(
                f"{len(logs)} "
                "registros exibidos"
            )
        )

        self._display_logs(
            logs
        )

    def _display_logs(
        self,
        logs: list[str],
    ) -> None:
        """Exibe os registros."""

        self.log_textbox.configure(
            state="normal"
        )

        self.log_textbox.delete(
            "1.0",
            "end",
        )

        if not logs:

            self.log_textbox.insert(
                "end",
                "Nenhum registro encontrado."
            )

        else:

            for line in logs:

                self.log_textbox.insert(
                    "end",
                    line + "\n\n",
                )

        self.log_textbox.configure(
            state="disabled"
        )

        self.log_textbox.yview_moveto(
            0.0
        )

    def _on_filter_changed(
        self,
        _value: str,
    ) -> None:
        """Atualiza a listagem após mudar o filtro."""

        self.refresh()