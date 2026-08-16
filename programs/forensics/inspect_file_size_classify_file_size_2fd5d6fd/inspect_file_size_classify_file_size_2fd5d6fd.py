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

def classify_file_size(file_size):
    """Classify a file based on its size."""
    if not file_size:
        return "unknown"

    size = file_size.get(
        "size_bytes",
        0,
    )

    if size < 1024:
        classification = "very_small"
    elif size < 1024 * 1024:
        classification = "small"
    elif size < 100 * 1024 * 1024:
        classification = "medium"
    else:
        classification = "large"

    return {
        "path": file_size.get("path"),
        "classification": classification,
        "size_bytes": size,
    }


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
    result_2 = classify_file_size(result)
    result = result_2

    display_success(result)


if __name__ == "__main__":
    main()
