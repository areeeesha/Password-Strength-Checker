# Password-Strength-Checker
A Python Password Strength Checker that analyzes password complexity, classifies strength, and provides security improvement suggestions.
# Password Strength Checker

A Python-based Password Strength Checker that evaluates password security using common cybersecurity best practices. The program analyzes password complexity based on length, uppercase letters, digits, and special characters, then classifies the password as **Weak**, **Medium**, or **Strong** while providing suggestions for improvement.

---

## Overview

This project is designed to help users evaluate the strength of their passwords using simple security validation techniques. It checks for essential password requirements and provides feedback to encourage stronger password creation.

---

## Features

- Checks password length (minimum 8 characters)
- Detects uppercase letters
- Detects numeric digits
- Detects special characters
- Classifies passwords as:
  - Weak
  - Medium
  - Strong
- Provides personalized improvement suggestions
- Interactive command-line interface
- Allows users to test multiple passwords

---

## Technologies Used

- Python 3
- Python `string` module

---

## Project Structure

```text
Password-Strength-Checker/
│
├── password_strength_checker.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/areeeesha/Password-Strength-Checker.git
```

Navigate to the project directory:

```bash
cd Password-Strength-Checker
```

---

## Usage

Run the program using Python:

```bash
python password_strength_checker.py
```

Follow the on-screen instructions to enter a password for evaluation.

---

## Example Output

```text
----------------------------------
    PASSWORD STRENGTH CHECKER
----------------------------------

Welcome to Areesha's Password Strength Checker!

Enter your password: Hello123

MEDIUM: Password meets two out of three criteria.

SUGGESTIONS:
Add at least one special character (!@#$%^&*()-+).
```

---

## How It Works

The program evaluates a password using the following criteria:

- Minimum length of 8 characters
- At least one uppercase letter
- At least one numeric digit
- At least one special character

Based on these checks, the password is classified as:

| Criteria Met | Strength |
|-------------:|----------|
| 0–1 | Weak |
| 2 | Medium |
| 3 | Strong |

For weak and medium passwords, the program also provides recommendations to improve password security.

---

## Learning Objectives

This project demonstrates the use of:

- Functions
- String manipulation
- Conditional statements
- Boolean logic
- Generator expressions (`any()`)
- User input handling
- Password validation techniques
- Basic cybersecurity principles

---

## Future Improvements

Potential enhancements include:

- Password entropy calculation
- Detection of commonly used passwords
- Password breach API integration
- Graphical User Interface (GUI)
- Password generator
- Password history analysis
- Color-coded terminal output

---

## Author

**Areesha Tahir**

Cybersecurity Intern | Computer Science Student | Python Developer

---

## License

This project is intended for educational purposes and was developed as part of a cybersecurity internship project at Decode Labs.
