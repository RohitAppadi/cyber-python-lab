"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import hashlib


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

def hash_text(text):
    """Generate a SHA-256 hash from text."""
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()

def describe_hash(hash_value):
    """Describe a hexadecimal hash value."""
    if not hash_value:
        return {
            "valid": False,
            "length": 0,
        }

    return {
        "valid": all(
            character in "0123456789abcdef"
            for character in hash_value.lower()
        ),
        "length": len(hash_value),
    }


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
    result_2 = decode_base64(result)
    result_3 = hash_text(result_2)
    result_4 = describe_hash(result_3)
    result = result_4

    display_result(result)


if __name__ == "__main__":
    main()
