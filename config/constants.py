"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : constants.py
---------------------------------------------------------
"""


from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT_DIR / "assets"

CONFIG_DIR = ROOT_DIR / "config"

DATABASE_DIR = ROOT_DIR / "database"

LOG_DIR = ROOT_DIR / "logs"

EXPORT_DIR = ROOT_DIR / "exports"

DOCS_DIR = ROOT_DIR / "docs"

TEMPLATE_DIR = ROOT_DIR / "templates"

TESTS_DIR = ROOT_DIR / "tests"

DATABASE_FILE = DATABASE_DIR / "caixaexpress.db"

CONFIG_FILE = CONFIG_DIR / "config.ini"

EMAIL_TEMPLATE = TEMPLATE_DIR / "email_template.html"