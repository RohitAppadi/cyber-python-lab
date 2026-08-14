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

def analyze_ip(ip_address):
    """Analyze basic IP address properties."""
    try:
        address = ipaddress.ip_address(
            ip_address
        )

        return {
            "address": str(address),
            "version": address.version,
            "private": address.is_private,
            "loopback": address.is_loopback,
            "multicast": address.is_multicast,
        }

    except ValueError:
        return None

def classify_ip(ip_information):
    """Classify an analyzed IP address."""
    if not ip_information:
        return {
            "classification": "invalid",
        }

    if ip_information.get("loopback"):
        classification = "loopback"
    elif ip_information.get("private"):
        classification = "private"
    elif ip_information.get("multicast"):
        classification = "multicast"
    else:
        classification = "public"

    return {
        "address": ip_information.get("address"),
        "version": ip_information.get("version"),
        "classification": classification,
    }

def summarize_ip_classification(ip_classification):
    """Create a concise IP classification summary."""
    if not ip_classification:
        return "No IP classification available."

    address = ip_classification.get(
        "address",
        "unknown",
    )

    classification = ip_classification.get(
        "classification",
        "unknown",
    )

    version = ip_classification.get(
        "version",
        "unknown",
    )

    return (
        f"{address} is a {classification} "
        f"IPv{version} address."
    )


def get_target_input():
    """Get a hostname or IP address from the user."""
    return input("Enter target hostname or IP: ").strip()


def display_result(value):
    """Display a result."""
    print(f"Result: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_target_input()

    result = resolve_hostname(input_value)
    result_2 = analyze_ip(result)
    result_3 = classify_ip(result_2)
    result_4 = summarize_ip_classification(result_3)
    result = result_4

    display_result(result)


if __name__ == "__main__":
    main()
