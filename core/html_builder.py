"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : html_builder.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela geração do conteúdo HTML utilizado
nos e-mails de fechamento de caixa.
---------------------------------------------------------
"""

from __future__ import annotations

from datetime import datetime
from html import escape


class HTMLBuilder:
    """Gera os conteúdos HTML dos e-mails do sistema."""

    @staticmethod
    def _format_currency(value: float) -> str:
        """Formata um valor para o padrão monetário brasileiro."""

        formatted = f"{value:,.2f}"

        formatted = (
            formatted
            .replace(",", "TEMP")
            .replace(".", ",")
            .replace("TEMP", ".")
        )

        return f"R$ {formatted}"

    @staticmethod
    def build_cash_report(
        store_name: str,
        cash_value: float,
        sent_at: datetime | None = None,
    ) -> str:
        """Gera o HTML do relatório de fechamento de caixa."""

        if sent_at is None:
            sent_at = datetime.now()

        safe_store_name = escape(
            store_name.strip()
        )

        formatted_value = (
            HTMLBuilder._format_currency(
                cash_value
            )
        )

        formatted_date = (
            sent_at.strftime("%d/%m/%Y")
        )

        formatted_time = (
            sent_at.strftime("%H:%M:%S")
        )

        return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
</head>

<body style="
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    font-family: Arial, Helvetica, sans-serif;
">

    <table
        width="100%"
        cellpadding="0"
        cellspacing="0"
        border="0"
        style="background-color: #f4f4f4;"
    >
        <tr>
            <td
                align="center"
                style="padding: 30px 15px;"
            >

                <table
                    width="600"
                    cellpadding="0"
                    cellspacing="0"
                    border="0"
                    style="
                        max-width: 600px;
                        background-color: #ffffff;
                        border: 1px solid #dddddd;
                        border-radius: 8px;
                    "
                >

                    <tr>
                        <td
                            style="
                                padding: 28px 35px;
                                text-align: center;
                                border-bottom: 1px solid #eeeeee;
                            "
                        >
                            <div
                                style="
                                    font-size: 24px;
                                    font-weight: bold;
                                    color: #333333;
                                "
                            >
                                Fechamento de Caixa
                            </div>

                            <div
                                style="
                                    margin-top: 7px;
                                    font-size: 14px;
                                    color: #777777;
                                "
                            >
                                Caixa Express
                            </div>
                        </td>
                    </tr>

                    <tr>
                        <td
                            style="
                                padding: 30px 35px;
                                color: #333333;
                            "
                        >

                            <div
                                style="
                                    font-size: 13px;
                                    color: #777777;
                                    margin-bottom: 5px;
                                "
                            >
                                Loja
                            </div>

                            <div
                                style="
                                    font-size: 20px;
                                    font-weight: bold;
                                    margin-bottom: 25px;
                                "
                            >
                                {safe_store_name}
                            </div>

                            <div
                                style="
                                    font-size: 13px;
                                    color: #777777;
                                    margin-bottom: 5px;
                                "
                            >
                                Valor do Caixa
                            </div>

                            <div
                                style="
                                    font-size: 28px;
                                    font-weight: bold;
                                    margin-bottom: 30px;
                                "
                            >
                                {formatted_value}
                            </div>

                            <table
                                width="100%"
                                cellpadding="0"
                                cellspacing="0"
                                border="0"
                            >
                                <tr>
                                    <td
                                        width="50%"
                                        style="
                                            font-size: 13px;
                                            color: #777777;
                                        "
                                    >
                                        Data
                                    </td>

                                    <td
                                        width="50%"
                                        style="
                                            font-size: 13px;
                                            color: #777777;
                                        "
                                    >
                                        Horário
                                    </td>
                                </tr>

                                <tr>
                                    <td
                                        style="
                                            padding-top: 5px;
                                            font-size: 16px;
                                            font-weight: bold;
                                            color: #333333;
                                        "
                                    >
                                        {formatted_date}
                                    </td>

                                    <td
                                        style="
                                            padding-top: 5px;
                                            font-size: 16px;
                                            font-weight: bold;
                                            color: #333333;
                                        "
                                    >
                                        {formatted_time}
                                    </td>
                                </tr>
                            </table>

                        </td>
                    </tr>

                    <tr>
                        <td
                            style="
                                padding: 20px 35px;
                                background-color: #fafafa;
                                border-top: 1px solid #eeeeee;
                                text-align: center;
                                font-size: 12px;
                                color: #888888;
                            "
                        >
                            Relatório gerado automaticamente
                            pelo Caixa Express.
                        </td>
                    </tr>

                </table>

            </td>
        </tr>
    </table>

</body>
</html>
""".strip()