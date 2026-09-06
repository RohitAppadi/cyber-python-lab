"""
Automatically generated cybersecurity utility.

Category: forensics
"""

import hashlib


def hash_file(file_path):
    """Calculate a SHA-256 hash for a file."""
    hasher = hashlib.sha256()

    try:
        with open(
            file_path,
            "rb",
        ) as file:

            for chunk in iter(
                lambda: file.read(4096),
                b"",
            ):
                hasher.update(chunk)

        return hasher.hexdigest()

    except OSError:
        return None


def get_file_input():
    """Get a file path from the user."""
    return input("Enter file path: ").strip()


def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_file_input()

    result = hash_file(input_value)

    display_warning(result)


if __name__ == "__main__":
    main()
