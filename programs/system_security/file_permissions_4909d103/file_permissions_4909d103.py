"""
Automatically generated cybersecurity utility.

Category: system_security
"""

import os
import stat


def file_permissions(file_path):
    """Inspect basic file permissions."""
    try:
        mode = os.stat(
            file_path
        ).st_mode

        return {
            "readable": os.access(
                file_path,
                os.R_OK,
            ),
            "writable": os.access(
                file_path,
                os.W_OK,
            ),
            "executable": os.access(
                file_path,
                os.X_OK,
            ),
            "mode": stat.filemode(mode),
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

    result = file_permissions(input_value)

    display_success(result)


if __name__ == "__main__":
    main()
