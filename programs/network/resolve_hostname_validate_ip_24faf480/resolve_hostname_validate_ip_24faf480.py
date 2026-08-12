"""
Automatically generated cybersecurity utility.

Category: network
"""

import ipaddress
import socket


def resolve_hostname(hostname):
    """Resolve a hostname to an IP address."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def validate_ip(ip_address):
    """Validate an IP address."""
    try:
        address = ipaddress.ip_address(
            ip_address
        )

        return {
            "address": str(address),
            "version": address.version,
            "valid": True,
        }

    except ValueError:
        return {
            "address": ip_address,
            "valid": False,
        }


def get_target_input():
    """Get a hostname or IP address from the user."""
    return input("Enter target hostname or IP: ").strip()


def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_target_input()

    result = resolve_hostname(input_value)
    result_2 = validate_ip(result)
    result = result_2

    display_warning(result)


if __name__ == "__main__":
    main()
