import string
import secrets
import math
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

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    validate_input(length, use_upper, use_lower, use_digits, use_symbols)
    pool = build_character_pool(
        use_upper, 
        use_lower, 
        use_digits, 
        use_symbols)
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
    return ''.join(password_chars)


def calculate_entropy(length, use_upper, use_lower, use_digits, use_symbols):
    pool_size = 0
    if use_upper:
        pool_size += len(UPPERCASE)
    if use_lower:
        pool_size += len(LOWERCASE)
    if use_digits:
        pool_size += len(DIGITS)
    if use_symbols:
        pool_size += len(SYMBOLS)
    if pool_size == 0:
        raise ValueError("At least one character type must be selected to calculate entropy.")
    entropy = length * math.log2(pool_size)
    return entropy

def classify_strength(entropy):
    WEAK_THRESHOLD = 40
    MODERATE_THRESHOLD = 60
    STRONG_THRESHOLD = 80
    if entropy < WEAK_THRESHOLD:
        return "Weak"
    elif entropy < MODERATE_THRESHOLD:
        return "Moderate"
    elif entropy < STRONG_THRESHOLD:
        return "Strong"
    else:
        return "Very Strong"
