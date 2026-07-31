"""
---------------------------------------------------------
Projeto : Caixa Express
Arquivo : auth_manager.py
Autor   : Dylan Ryan Pereira Santos
Versão  : 0.1.0
---------------------------------------------------------
Descrição:
Responsável pela autenticação administrativa do sistema.
As senhas são armazenadas utilizando PBKDF2-HMAC-SHA256.
---------------------------------------------------------
"""

from __future__ import annotations

import hashlib
import hmac
import secrets


class AuthManager:
    """Gerencia autenticação e hash de senhas."""

    ALGORITHM = "sha256"
    ITERATIONS = 600_000
    SALT_SIZE = 16

    @classmethod
    def create_password_hash(
        cls,
        password: str,
    ) -> str:
        """Cria um hash seguro para uma senha."""

        if not password:
            raise ValueError(
                "A senha não pode estar vazia."
            )

        salt = secrets.token_bytes(
            cls.SALT_SIZE
        )

        password_hash = hashlib.pbkdf2_hmac(
            cls.ALGORITHM,
            password.encode("utf-8"),
            salt,
            cls.ITERATIONS,
        )

        return (
            f"pbkdf2_{cls.ALGORITHM}"
            f"${cls.ITERATIONS}"
            f"${salt.hex()}"
            f"${password_hash.hex()}"
        )

    @classmethod
    def verify_password(
        cls,
        password: str,
        stored_hash: str,
    ) -> bool:
        """Valida uma senha contra o hash armazenado."""

        if not password or not stored_hash:
            return False

        try:
            (
                algorithm_name,
                iterations_text,
                salt_hex,
                expected_hash_hex,
            ) = stored_hash.split("$")

            expected_algorithm = (
                f"pbkdf2_{cls.ALGORITHM}"
            )

            if algorithm_name != expected_algorithm:
                return False

            iterations = int(
                iterations_text
            )

            salt = bytes.fromhex(
                salt_hex
            )

            expected_hash = bytes.fromhex(
                expected_hash_hex
            )

            calculated_hash = hashlib.pbkdf2_hmac(
                cls.ALGORITHM,
                password.encode("utf-8"),
                salt,
                iterations,
            )

            return hmac.compare_digest(
                calculated_hash,
                expected_hash,
            )

        except (
            ValueError,
            TypeError,
        ):
            return False