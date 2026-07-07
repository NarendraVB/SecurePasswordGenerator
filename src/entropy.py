import math
from src.generator import UPPERCASE, LOWERCASE, DIGITS, SYMBOLS

WEAK_THRESHOLD = 40
MODERATE_THRESHOLD = 60
STRONG_THRESHOLD = 80


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
        raise ValueError("Character pool cannot be empty.")

    return length * math.log2(pool_size)


def classify_strength(entropy):

    if entropy < WEAK_THRESHOLD:
        return "Weak"

    elif entropy < MODERATE_THRESHOLD:
        return "Moderate"

    elif entropy < STRONG_THRESHOLD:
        return "Strong"

    return "Very Strong"