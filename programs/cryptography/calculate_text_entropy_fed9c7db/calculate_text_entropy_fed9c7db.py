"""
Automatically generated cybersecurity utility.

Category: cryptography
"""

import math


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


def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = calculate_text_entropy(input_value)

    display_warning(result)


if __name__ == "__main__":
    main()
