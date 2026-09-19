"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import base64
import math


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


def get_encoded_text_input():
    """Get encoded text from the user."""
    return input("Enter Base64 encoded text: ").strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_encoded_text_input()

    result = decode_base64(input_value)
    result_2 = calculate_text_entropy(result)
    result = result_2

    display_result(result)


if __name__ == "__main__":
    main()
