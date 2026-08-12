"""
Automatically generated cybersecurity utility.

Category: web_security
"""

import re


def extract_urls(text):
    """Extract URLs from text."""
    pattern = r"https?://[^\s]+"

    return re.findall(
        pattern,
        text,
    )


def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = extract_urls(input_value)

    display_result(result)


if __name__ == "__main__":
    main()
