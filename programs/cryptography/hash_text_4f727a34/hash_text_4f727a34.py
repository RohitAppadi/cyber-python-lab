"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import hashlib


def hash_text(text):
    """Generate a SHA-256 hash from text."""
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()


def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = hash_text(input_value)

    display_warning(result)


if __name__ == "__main__":
    main()
