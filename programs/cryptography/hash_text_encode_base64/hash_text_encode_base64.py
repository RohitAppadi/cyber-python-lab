"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import hashlib


def hash_text(text, algorithm="sha256"):
    """Return the hexadecimal digest of text."""
    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        return None

    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()

def encode_base64(text):
    """Encode text using Base64."""
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")


def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = hash_text(input_value)
    result_2 = encode_base64(result)
    result = result_2

    display_result(result)


if __name__ == "__main__":
    main()
