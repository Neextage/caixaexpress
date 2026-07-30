"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : main.py
Autor   : Dylan Ryan Pereira Santos
---------------------------------------------------------
"""

from config.version import AppInfo


def main() -> None:
    print("=" * 50)
    print(AppInfo.NAME)
    print(f"Versão : {AppInfo.VERSION}")
    print(f"Build   : {AppInfo.BUILD}")
    print("=" * 50)


if __name__ == "__main__":
    main()