"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64


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

    result = encode_base64(input_value)

    display_result(result)


if __name__ == "__main__":
    main()
