"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64


def decode_base64(encoded_text):
    """Decode Base64 encoded text."""
    try:
        return base64.b64decode(
            encoded_text
        ).decode("utf-8")

    except Exception:
        return None


def get_encoded_text_input():
    """Get encoded text from the user."""
    return input("Enter Base64 encoded text: ").strip()


def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_encoded_text_input()

    result = decode_base64(input_value)

    display_warning(result)


if __name__ == "__main__":
    main()
