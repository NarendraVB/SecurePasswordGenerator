import string
import secrets

MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 128

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation


class Generator:

    @staticmethod
    def validate_input(length, use_upper, use_lower, use_digits, use_symbols):

        if not isinstance(length, int):
            raise ValueError("Password length must be an integer.")

        selected_sets = (
            use_upper
            + use_lower
            + use_digits
            + use_symbols
        )

        if selected_sets == 0:
            raise ValueError("At least one character type must be selected.")

        if length < MIN_PASSWORD_LENGTH:
            raise ValueError(
                f"Password length must be at least {MIN_PASSWORD_LENGTH} characters."
            )

        if length > MAX_PASSWORD_LENGTH:
            raise ValueError(
                f"Password length must not exceed {MAX_PASSWORD_LENGTH} characters."
            )

        if length < selected_sets:
            raise ValueError(
                "Password length must be greater than or equal to the number of selected character types."
            )

    @staticmethod
    def build_character_pool(use_upper, use_lower, use_digits, use_symbols):

        pool = ""

        if use_upper:
            pool += UPPERCASE

        if use_lower:
            pool += LOWERCASE

        if use_digits:
            pool += DIGITS

        if use_symbols:
            pool += SYMBOLS

        return pool

    @staticmethod
    def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

        Generator.validate_input(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
        )

        pool = Generator.build_character_pool(
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
        )

        password_chars = []

        if use_upper:
            password_chars.append(secrets.choice(UPPERCASE))

        if use_lower:
            password_chars.append(secrets.choice(LOWERCASE))

        if use_digits:
            password_chars.append(secrets.choice(DIGITS))

        if use_symbols:
            password_chars.append(secrets.choice(SYMBOLS))

        while len(password_chars) < length:
            password_chars.append(secrets.choice(pool))

        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)