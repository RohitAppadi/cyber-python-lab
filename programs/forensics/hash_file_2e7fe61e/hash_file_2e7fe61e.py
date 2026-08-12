"""
Automatically generated cybersecurity utility.

Category: forensics
"""

from pathlib import Path
import hashlib


def hash_file(file_path):
    """Calculate the SHA-256 hash of a file."""
    path = Path(file_path)

    if not path.is_file():
        return None

    hasher = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_file_input():
    """Get a file path from the user."""
    return input("Enter file path: ").strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_file_input()

    result = hash_file(input_value)

    display_result(result)


if __name__ == "__main__":
    main()
