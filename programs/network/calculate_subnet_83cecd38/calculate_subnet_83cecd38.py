"""
Automatically generated cybersecurity utility.

Category: network
"""

import ipaddress


def calculate_subnet(network):
    """Return basic information about an IP network."""
    try:
        net = ipaddress.ip_network(network, strict=False)

        return {
            "network": str(net.network_address),
            "broadcast": str(net.broadcast_address),
            "netmask": str(net.netmask),
            "hosts": net.num_addresses,
        }
    except ValueError:
        return None


def get_network_input():
    """Get an IP network from the user."""
    return input("Enter IP network (example: 192.168.1.0/24): ").strip()


def display_dictionary(data):
    """Display dictionary data."""
    if data is None:
        print("No data available.")
        return

    for key, value in data.items():
        print(f"{key}: {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_network_input()

    result = calculate_subnet(input_value)

    display_dictionary(result)


if __name__ == "__main__":
    main()
