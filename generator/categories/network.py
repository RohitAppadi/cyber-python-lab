"""
Network security function components.
"""

NETWORK_FUNCTIONS = [

    {
        "name": "resolve_hostname",
        "category": "network",
        "description": (
            "Resolve a hostname to its corresponding IP address."
        ),
        "requires": ["hostname"],
        "provides": ["ip_address"],
        "dependencies": ["socket"],
        "code": '''def resolve_hostname(hostname):
    """Resolve a hostname to an IP address."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None
''',
    },

    {
        "name": "calculate_subnet",
        "category": "network",
        "description": (
            "Calculate basic information about an IP network."
        ),
        "requires": ["network"],
        "provides": ["subnet_information"],
        "dependencies": ["ipaddress"],
        "code": '''def calculate_subnet(network):
    """Return basic information about an IP network."""
    try:
        net = ipaddress.ip_network(
            network,
            strict=False,
        )

        return {
            "network": str(net.network_address),
            "broadcast": str(net.broadcast_address),
            "netmask": str(net.netmask),
            "hosts": net.num_addresses,
        }

    except ValueError:
        return None
''',
    },

    {
        "name": "validate_ip",
        "category": "network",
        "description": (
            "Validate whether a value is a valid IP address."
        ),
        "requires": ["ip_address"],
        "provides": ["ip_validation"],
        "dependencies": ["ipaddress"],
        "code": '''def validate_ip(ip_address):
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
''',
    },

    {
        "name": "analyze_ip",
        "category": "network",
        "description": (
            "Analyze basic properties of an IP address."
        ),
        "requires": ["ip_address"],
        "provides": ["ip_information"],
        "dependencies": ["ipaddress"],
        "code": '''def analyze_ip(ip_address):
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
''',
    },

    {
        "name": "classify_ip",
        "category": "network",
        "description": (
            "Classify an IP address based on common network properties."
        ),
        "requires": ["ip_information"],
        "provides": ["ip_classification"],
        "dependencies": [],
        "code": '''def classify_ip(ip_information):
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
''',
    },

    {
        "name": "summarize_ip_classification",
        "category": "network",
        "description": (
            "Create a concise summary of an IP classification."
        ),
        "requires": ["ip_classification"],
        "provides": ["network_summary"],
        "dependencies": [],
        "code": '''def summarize_ip_classification(ip_classification):
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
''',
    },

    {
        "name": "extract_domain",
        "category": "network",
        "description": (
            "Extract a domain name from a URL."
        ),
        "requires": ["url"],
        "provides": ["domain"],
        "dependencies": ["urllib"],
        "code": '''def extract_domain(url):
    """Extract a domain from a URL."""
    parsed = urlparse(url)

    if not parsed.netloc:
        return None

    return parsed.netloc.split(":")[0]
''',
    },

    {
        "name": "domain_to_hostname",
        "category": "network",
        "description": (
            "Convert an extracted domain into a hostname value."
        ),
        "requires": ["domain"],
        "provides": ["hostname"],
        "dependencies": [],
        "code": '''def domain_to_hostname(domain):
    """Treat a domain as a hostname for DNS resolution."""
    if not domain:
        return None

    return domain.strip().lower()
''',
    },
]