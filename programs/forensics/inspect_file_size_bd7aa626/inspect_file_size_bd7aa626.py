"""
Automatically generated cybersecurity utility.

Category: forensics
"""

import os


def inspect_file_size(file_path):
    """Return the size of a file in bytes."""
    try:
        return {
            "path": file_path,
            "size_bytes": os.path.getsize(
                file_path
            ),
        }

    except OSError:
        return None


def get_file_input():
    """Get a file path from the user."""
    return input("Enter file path: ").strip()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_file_input()

    result = inspect_file_size(input_value)

    display_success(result)


if __name__ == "__main__":
    main()
