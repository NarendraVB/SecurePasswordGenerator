# 🔐 Secure Password Generator

A professional command-line password generator built using Python that creates cryptographically secure passwords using Python's `secrets` module.

Unlike traditional random generators, this project uses a Cryptographically Secure Pseudo-Random Number Generator (CSPRNG) to generate passwords suitable for authentication systems, user accounts, API keys, and enterprise environments.

---

# Overview

Weak passwords remain one of the leading causes of security breaches. Attackers exploit predictable passwords using brute-force attacks, dictionary attacks, credential stuffing, and password spraying.

This project demonstrates how security engineers generate strong passwords using cryptographically secure randomness while also calculating password entropy and classifying password strength.

---

# Cybersecurity Concepts

- Authentication
- Password Security
- Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)
- Entropy
- Search Space
- Password Policies
- Brute Force Attacks
- Dictionary Attacks
- Password Complexity
- Password Strength Evaluation

---

# Attacker Perspective

Attackers attempt to compromise accounts by guessing passwords through:

- Brute Force Attacks
- Dictionary Attacks
- Password Spraying
- Credential Stuffing

If passwords are predictable or generated using insecure random number generators, attackers can significantly reduce the search space and improve their chances of success.

---

# Defender Perspective

Security engineers defend against password attacks by:

- Using cryptographically secure random number generators
- Increasing password entropy
- Enforcing password policies
- Increasing search space
- Encouraging long random passwords
- Using password managers

---

# Features

- Cryptographically Secure Password Generation
- Configurable Password Length
- Uppercase Letters
- Lowercase Letters
- Numbers
- Symbols
- Input Validation
- Entropy Calculation
- Password Strength Classification
- Interactive Command-Line Interface

---

# Project Structure

```
SecurePasswordGenerator/

├── src/
│   ├── __init__.py
│   ├── generator.py
│   ├── entropy.py
│   └── cli.py
│
├── tests/
│   └── test_generator.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

```bash
git clone https://github.com/<your-username>/SecurePasswordGenerator.git

cd SecurePasswordGenerator

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

# Usage

```bash
python main.py
```

Example:

```
==========================================
      Secure Password Generator
==========================================

Enter password length: 16

Include uppercase? (y/n): y

Include lowercase? (y/n): y

Include digits? (y/n): y

Include symbols? (y/n): y

==========================================

Generated Password : !N6@uK7#hLm$Q9rP

Length             : 16

Entropy            : 104.87 bits

Strength           : Very Strong
```

---

# Cybersecurity Concepts Learned

- Why `random` should never be used for password generation
- Cryptographically Secure Random Number Generators
- Password Entropy
- Password Search Space
- Password Policies
- Secure Password Generation
- Password Complexity
- Input Validation
- Secure Software Design

---

# What I Learned

- Building secure software requires understanding attacker behavior.
- Cryptographic randomness is fundamentally different from pseudo-randomness.
- Password strength depends on both password length and character pool size.
- Security tools should fail safely through proper validation.
- Modular software design improves maintainability and testing.

---

# Future Improvements

- Password History Check
- Common Password Detection
- Password Policy Profiles
- Password Manager Integration
- Password Copy to Clipboard
- QR Code Export
- GUI Version
- Password Expiration Suggestions
- Passphrase Generator
- Bulk Password Generation

---

# Disclaimer

This project is intended for educational purposes and demonstrates secure password generation techniques using Python's cryptographic libraries.