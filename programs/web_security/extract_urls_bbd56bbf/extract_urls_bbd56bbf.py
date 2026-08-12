"""
Automatically generated cybersecurity utility.

Category: web_security
"""

import re


def extract_urls(text):
    """Extract HTTP and HTTPS URLs from text."""
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_text_input()

    result = extract_urls(input_value)

    display_success(result)


if __name__ == "__main__":
    main()
