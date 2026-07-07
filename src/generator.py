import string
def validate_input(length, use_upper, use_lower, use_digits, use_symbols):
    selected_sets = (
    use_upper +
    use_lower +
    use_digits +
    use_symbols
    )
    MIN_PASSWORD_LENGTH = 4
    MAX_PASSWORD_LENGTH = 128
    if not isinstance(length, int):
        raise ValueError("Password length must be an integer.")
    if selected_sets == 0:
        raise ValueError("At least one character type must be selected.")
    if length < MIN_PASSWORD_LENGTH:
        raise ValueError("Password length must be at least 4 characters.")
    if length > MAX_PASSWORD_LENGTH:
        raise ValueError("Password length must not exceed 128 characters.") 
    if length < selected_sets:
        raise ValueError("Password length must be greater than or equal to the number of selected character types.")
    

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation

def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = []
    if use_upper:
        pool.append(UPPERCASE)
    if use_lower:
        pool.append(LOWERCASE)
    if use_digits:
        pool.append(DIGITS)
    if use_symbols:
        pool.append(SYMBOLS)
    return pool
