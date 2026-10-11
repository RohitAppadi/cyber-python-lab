"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64


def encode_base64(text):
    """Encode text using Base64."""
    return base64.b64encode(
        text.encode("utf-8")
    ).decode("utf-8")

def decode_base64(encoded_text):
    """Decode Base64 encoded text."""
    try:
        return base64.b64decode(
            encoded_text
        ).decode("utf-8")

    except Exception:
        return None


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
    result_2 = decode_base64(result)
    result = result_2

    display_success(result)


if __name__ == "__main__":
    main()
