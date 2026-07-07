from generator import Generator


def test_password_length():

    password = Generator.generate_password(
        16,
        True,
        True,
        True,
        True,
    )

    assert len(password) == 16


def test_uppercase():

    password = Generator.generate_password(
        12,
        True,
        False,
        False,
        False,
    )

    assert any(c.isupper() for c in password)


def test_lowercase():

    password = Generator.generate_password(
        12,
        False,
        True,
        False,
        False,
    )

    assert any(c.islower() for c in password)


def test_digits():

    password = Generator.generate_password(
        12,
        False,
        False,
        True,
        False,
    )

    assert any(c.isdigit() for c in password)


def test_symbols():

    password = Generator.generate_password(
        12,
        False,
        False,
        False,
        True,
    )

    assert any(not c.isalnum() for c in password)