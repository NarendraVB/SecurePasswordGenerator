def get_yes_no(prompt):

    while True:

        choice = input(prompt).strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter y/yes or n/no.")


def get_user_input():

    while True:

        try:

            length = int(
                input("Enter password length (4-128): ")
            )

            use_upper = get_yes_no(
                "Include uppercase letters? (y/n): "
            )

            use_lower = get_yes_no(
                "Include lowercase letters? (y/n): "
            )

            use_digits = get_yes_no(
                "Include digits? (y/n): "
            )

            use_symbols = get_yes_no(
                "Include symbols? (y/n): "
            )

            return (
                length,
                use_upper,
                use_lower,
                use_digits,
                use_symbols,
            )

        except ValueError:

            print("Password length must be an integer.")