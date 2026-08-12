"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import hashlib


def encode_base64(text):
    """Encode text using Base64."""
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")

def hash_text(text, algorithm="sha256"):
    """Return the hexadecimal digest of text."""
    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        return None

    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = encode_base64(input_value)
    result_2 = hash_text(result)
    result = result_2

    display_success(result)


if __name__ == "__main__":
    main()
