"""
Automatically generated cybersecurity utility.

Category: system_security
"""

import os


def file_permissions(file_path):
    """Return basic permission information for a file."""
    if not os.path.exists(file_path):
        return None

    return {
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK),
    }


def get_file_input():
    """Get a file path from the user."""
    return input("Enter file path: ").strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_file_input()

    result = file_permissions(input_value)

    display_result(result)


if __name__ == "__main__":
    main()
