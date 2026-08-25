"""
Automatically generated cybersecurity utility.

Category: forensics
"""

import math


def calculate_entropy(text):
    """Calculate Shannon entropy."""
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


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = calculate_entropy(input_value)

    display_result(result)


if __name__ == "__main__":
    main()
