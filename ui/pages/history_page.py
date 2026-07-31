"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : history_page.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Página administrativa responsável pela visualização
do histórico de envios do Caixa Express.
---------------------------------------------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme import ThemeColors
from core.database import DatabaseManager


class HistoryPage(ctk.CTkFrame):
    """Página de histórico de envios."""

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

        self._create_interface()

    def _create_interface(self) -> None:
        """Cria a interface da página."""

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
            text="Histórico",
            font=("Segoe UI", 28, "bold"),
            text_color=ThemeColors.TEXT,
        )

        title.pack(
            anchor="w",
        )

        description = ctk.CTkLabel(
            title_area,
            text=(
                "Acompanhe as tentativas de envio "
                "dos relatórios de caixa."
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

        self._create_summary()
        self._create_table_header()

        self.list_frame = (
            ctk.CTkScrollableFrame(
                self,
                fg_color="transparent",
                corner_radius=0,
            )
        )

        self.list_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=(0, 30),
        )

    def _create_summary(self) -> None:
        """Cria os indicadores superiores."""

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
            (0, 1, 2),
            weight=1,
        )

        self.total_card = self._create_summary_card(
            summary,
            0,
            "Total",
            "0",
            ThemeColors.PRIMARY,
        )

        self.success_card = self._create_summary_card(
            summary,
            1,
            "Sucessos",
            "0",
            ThemeColors.SUCCESS,
        )

        self.error_card = self._create_summary_card(
            summary,
            2,
            "Erros",
            "0",
            ThemeColors.ERROR,
        )

    def _create_summary_card(
        self,
        master,
        column: int,
        title: str,
        value: str,
        value_color: str,
    ) -> ctk.CTkLabel:
        """Cria um indicador do histórico."""

        card = ctk.CTkFrame(
            master,
            height=85,
            corner_radius=12,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=(
                0 if column == 0 else 5,
                0 if column == 2 else 5,
            ),
        )

        card.grid_propagate(
            False
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 12),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        title_label.pack(
            anchor="w",
            padx=18,
            pady=(13, 0),
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 22, "bold"),
            text_color=value_color,
        )

        value_label.pack(
            anchor="w",
            padx=18,
        )

        return value_label

    def _create_table_header(self) -> None:
        """Cria o cabeçalho da listagem."""

        header = ctk.CTkFrame(
            self,
            height=42,
            corner_radius=8,
            fg_color=ThemeColors.PRIMARY,
        )

        header.pack(
            fill="x",
            padx=45,
            pady=(0, 5),
        )

        header.pack_propagate(
            False
        )

        columns = [
            ("Protocolo", 145),
            ("Loja", 180),
            ("Valor", 110),
            ("Data", 95),
            ("Hora", 75),
            ("Status", 100),
        ]

        for text, width in columns:

            label = ctk.CTkLabel(
                header,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 11, "bold"),
                text_color="#FFFFFF",
            )

            label.pack(
                side="left",
                padx=(10, 0),
            )

    def refresh(self) -> None:
        """Atualiza o histórico."""

        self._clear_history()

        history = (
            self._database
            .get_history()
        )

        summary = (
            self._database
            .get_history_summary()
        )

        self.total_card.configure(
            text=str(
                summary["total"]
            )
        )

        self.success_card.configure(
            text=str(
                summary["success"]
            )
        )

        self.error_card.configure(
            text=str(
                summary["errors"]
            )
        )

        if not history:
            self._create_empty_state()
            return

        for record in history:
            self._create_history_row(
                record
            )

    def _clear_history(self) -> None:
        """Limpa a listagem atual."""

        for widget in (
            self.list_frame
            .winfo_children()
        ):
            widget.destroy()

    def _create_history_row(
        self,
        record,
    ) -> None:
        """Cria uma linha do histórico."""

        row = ctk.CTkFrame(
            self.list_frame,
            corner_radius=8,
            fg_color=ThemeColors.SURFACE,
            border_width=1,
            border_color=ThemeColors.BORDER,
        )

        row.pack(
            fill="x",
            pady=3,
        )

        status = (
            record["status"]
            or ""
        ).strip()

        status_upper = (
            status.upper()
        )

        if status_upper in {
            "SUCESSO",
            "ENVIADO",
        }:
            status_color = (
                ThemeColors.SUCCESS
            )
        else:
            status_color = (
                ThemeColors.ERROR
            )

        values = [
            (
                record["protocol"]
                or "-",
                145,
                ThemeColors.TEXT,
            ),
            (
                record["store_name"]
                or "-",
                180,
                ThemeColors.TEXT,
            ),
            (
                self._format_currency(
                    record["cash_value"]
                ),
                110,
                ThemeColors.TEXT,
            ),
            (
                record["send_date"]
                or "-",
                95,
                ThemeColors.TEXT,
            ),
            (
                record["send_time"]
                or "-",
                75,
                ThemeColors.TEXT,
            ),
            (
                status or "-",
                100,
                status_color,
            ),
        ]

        for text, width, color in values:

            label = ctk.CTkLabel(
                row,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 11),
                text_color=color,
            )

            label.pack(
                side="left",
                padx=(10, 0),
                pady=10,
            )

        message = (
            record["message"]
            or ""
        ).strip()

        if message:

            message_label = ctk.CTkLabel(
                row,
                text=message,
                anchor="w",
                font=("Segoe UI", 10),
                text_color=ThemeColors.TEXT_LIGHT,
            )

            message_label.pack(
                fill="x",
                padx=10,
                pady=(0, 8),
            )

    def _create_empty_state(self) -> None:
        """Exibe mensagem sem registros."""

        message = ctk.CTkLabel(
            self.list_frame,
            text="Nenhum envio registrado.",
            font=("Segoe UI", 14),
            text_color=ThemeColors.TEXT_LIGHT,
        )

        message.pack(
            pady=60,
        )

    @staticmethod
    def _format_currency(
        value,
    ) -> str:
        """Formata valor para moeda brasileira."""

        try:
            number = float(value or 0)

        except (
            TypeError,
            ValueError,
        ):
            number = 0

        formatted = (
            f"{number:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"R$ {formatted}"