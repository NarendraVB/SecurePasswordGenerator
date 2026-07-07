from src.generator import Generator
from src.entropy import calculate_entropy, classify_strength
from src.cli import get_user_input


def main():

    print("=" * 45)
    print("      Secure Password Generator")
    print("=" * 45)

    try:

        (
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
        ) = get_user_input()

        password = Generator.generate_password(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
        )

        entropy = calculate_entropy(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols,
        )

        strength = classify_strength(entropy)

        print("\n" + "=" * 45)
        print(f"Generated Password : {password}")
        print(f"Length             : {length}")
        print(f"Entropy            : {entropy:.2f} bits")
        print(f"Strength           : {strength}")

        print("\nCharacter Sets")
        print("-" * 20)

        if use_upper:
            print("✓ Uppercase")

        if use_lower:
            print("✓ Lowercase")

        if use_digits:
            print("✓ Digits")

        if use_symbols:
            print("✓ Symbols")

        print("=" * 45)

    except ValueError as e:

        print(f"\nError: {e}")


if __name__ == "__main__":
    main()