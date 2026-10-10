"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import hashlib


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


def get_encoded_text_input():
    """Get encoded text from the user."""
    return input("Enter Base64 encoded text: ").strip()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_encoded_text_input()

    result = decode_base64(input_value)
    result_2 = hash_text(result)
    result_3 = describe_hash(result_2)
    result = result_3

    display_success(result)


if __name__ == "__main__":
    main()
