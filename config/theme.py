"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : theme.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
Data    : 30/07/2026
---------------------------------------------------------
Descrição:
Centraliza todas as configurações visuais da aplicação.
---------------------------------------------------------
"""


class ThemeColors:
    """Paleta oficial do Caixa Express."""

    PRIMARY = "#121C4F"
    SECONDARY = "#802328"

    BACKGROUND = "#F5F5F5"
    SURFACE = "#FFFFFF"

    TEXT = "#1F2937"
    TEXT_LIGHT = "#6B7280"

    SUCCESS = "#16A34A"
    WARNING = "#F59E0B"
    ERROR = "#DC2626"

    BORDER = "#DCDCDC"

    BUTTON_TEXT = "#FFFFFF"


class ThemeFonts:
    """Fontes utilizadas na aplicação."""

    FAMILY = "Segoe UI"

    TITLE = (FAMILY, 24, "bold")

    SUBTITLE = (FAMILY, 18, "bold")

    TEXT = (FAMILY, 14)

    SMALL = (FAMILY, 12)

    BUTTON = (FAMILY, 14, "bold")


class ThemeSizes:
    """Dimensões padrão."""

    WINDOW_WIDTH = 900

    WINDOW_HEIGHT = 650

    MIN_WIDTH = 900

    MIN_HEIGHT = 650

    BUTTON_HEIGHT = 42

    BUTTON_WIDTH = 220

    ENTRY_HEIGHT = 38

    BORDER_RADIUS = 10

    PADDING = 20