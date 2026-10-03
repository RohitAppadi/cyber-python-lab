"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import math


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

def calculate_text_entropy(text):
    """Calculate Shannon entropy for text."""
    if not text:
        return 0.0

    frequency = {}

    for character in text:
        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    length = len(text)
    entropy = 0.0

    for count in frequency.values():
        probability = count / length

        entropy -= (
            probability * math.log2(probability)
        )

    return entropy


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
    result_3 = calculate_text_entropy(result_2)
    result = result_3

    display_success(result)


if __name__ == "__main__":
    main()
