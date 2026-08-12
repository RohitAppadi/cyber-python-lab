"""
Automatically generated cybersecurity utility.

Category: network
"""

import socket


def resolve_hostname(hostname):
    """Resolve a hostname to an IP address."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None


def get_target_input():
    """Get a hostname or IP address from the user."""
    return input("Enter target hostname or IP: ").strip()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_target_input()

    result = resolve_hostname(input_value)

    display_success(result)


if __name__ == "__main__":
    main()
