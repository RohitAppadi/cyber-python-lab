"""
Cybersecurity function components.

Each function declares:

- name
- category
- description
- requires
- provides
- dependencies
- code
"""

FUNCTION_COMPONENTS = [

    # ============================================================
    # NETWORK
    # ============================================================

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

    # ============================================================
    # CRYPTOGRAPHY
    # ============================================================

    {
        "name": "hash_text",
        "category": "cryptography",
        "description": (
            "Generate a SHA-256 hash from text."
        ),
        "requires": ["text"],
        "provides": ["hash"],
        "dependencies": ["hashlib"],
        "code": '''def hash_text(text):
    """Generate a SHA-256 hash from text."""
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()
''',
    },

    {
        "name": "encode_base64",
        "category": "cryptography",
        "description": (
            "Encode text using Base64."
        ),
        "requires": ["text"],
        "provides": ["encoded_text"],
        "dependencies": ["base64"],
        "code": '''def encode_base64(text):
    """Encode text using Base64."""
    return base64.b64encode(
        text.encode("utf-8")
    ).decode("utf-8")
''',
    },

    {
        "name": "decode_base64",
        "category": "cryptography",
        "description": (
            "Decode Base64 encoded text."
        ),
        "requires": ["encoded_text"],
        "provides": ["text"],
        "dependencies": ["base64"],
        "code": '''def decode_base64(encoded_text):
    """Decode Base64 encoded text."""
    try:
        return base64.b64decode(
            encoded_text
        ).decode("utf-8")

    except Exception:
        return None
''',
    },

    {
        "name": "calculate_text_entropy",
        "category": "cryptography",
        "description": (
            "Calculate Shannon entropy for text."
        ),
        "requires": ["text"],
        "provides": ["entropy"],
        "dependencies": ["math"],
        "code": '''def calculate_text_entropy(text):
    """Calculate Shannon entropy for text."""
    if not text:
        return 0.0

    frequency = {}

    for character in text:
        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    length = len(text)
    entropy = 0.0

    for count in frequency.values():
        probability = count / length

        entropy -= (
            probability * math.log2(probability)
        )

    return entropy
''',
    },

    {
        "name": "describe_hash",
        "category": "cryptography",
        "description": (
            "Describe basic properties of a generated hash."
        ),
        "requires": ["hash"],
        "provides": ["hash_information"],
        "dependencies": [],
        "code": '''def describe_hash(hash_value):
    """Describe a hexadecimal hash value."""
    if not hash_value:
        return {
            "valid": False,
            "length": 0,
        }

    return {
        "valid": all(
            character in "0123456789abcdef"
            for character in hash_value.lower()
        ),
        "length": len(hash_value),
    }
''',
    },

    # ============================================================
    # FORENSICS
    # ============================================================

    {
        "name": "hash_file",
        "category": "forensics",
        "description": (
            "Calculate the SHA-256 hash of a file."
        ),
        "requires": ["file_path"],
        "provides": ["file_hash"],
        "dependencies": ["hashlib"],
        "code": '''def hash_file(file_path):
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
''',
    },

    {
        "name": "calculate_entropy",
        "category": "forensics",
        "description": (
            "Calculate Shannon entropy for text data."
        ),
        "requires": ["text"],
        "provides": ["entropy"],
        "dependencies": ["math"],
        "code": '''def calculate_entropy(text):
    """Calculate Shannon entropy."""
    if not text:
        return 0.0

    frequency = {}

    for character in text:
        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    length = len(text)
    entropy = 0.0

    for count in frequency.values():
        probability = count / length

        entropy -= (
            probability * math.log2(probability)
        )

    return entropy
''',
    },

    {
        "name": "inspect_file_size",
        "category": "forensics",
        "description": (
            "Inspect the size of a file."
        ),
        "requires": ["file_path"],
        "provides": ["file_size"],
        "dependencies": ["os"],
        "code": '''def inspect_file_size(file_path):
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
''',
    },

    {
        "name": "classify_file_size",
        "category": "forensics",
        "description": (
            "Classify a file based on its size."
        ),
        "requires": ["file_size"],
        "provides": ["file_size_classification"],
        "dependencies": [],
        "code": '''def classify_file_size(file_size):
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
''',
    },

    # ============================================================
    # WEB SECURITY
    # ============================================================

    {
        "name": "extract_urls",
        "category": "web_security",
        "description": (
            "Extract URLs from supplied text."
        ),
        "requires": ["text"],
        "provides": ["urls"],
        "dependencies": ["re"],
        "code": '''def extract_urls(text):
    """Extract URLs from text."""
    pattern = r"https?://[^\\s]+"

    return re.findall(
        pattern,
        text,
    )
''',
    },

    {
        "name": "count_urls",
        "category": "web_security",
        "description": (
            "Count URLs found in extracted URL data."
        ),
        "requires": ["urls"],
        "provides": ["url_count"],
        "dependencies": [],
        "code": '''def count_urls(urls):
    """Count extracted URLs."""
    return {
        "count": len(urls),
        "urls": urls,
    }
''',
    },

    # ============================================================
    # SYSTEM SECURITY
    # ============================================================

    {
        "name": "file_permissions",
        "category": "system_security",
        "description": (
            "Inspect basic permissions of a file."
        ),
        "requires": ["file_path"],
        "provides": ["permissions"],
        "dependencies": ["os", "stat"],
        "code": '''def file_permissions(file_path):
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
''',
    },

    {
        "name": "classify_permissions",
        "category": "system_security",
        "description": (
            "Classify basic file permission properties."
        ),
        "requires": ["permissions"],
        "provides": ["permission_classification"],
        "dependencies": [],
        "code": '''def classify_permissions(permissions):
    """Classify file permissions."""
    if not permissions:
        return {
            "classification": "unavailable",
        }

    if permissions.get("writable"):
        classification = "writable"

    elif permissions.get("executable"):
        classification = "executable"

    elif permissions.get("readable"):
        classification = "readable"

    else:
        classification = "restricted"

    return {
        "classification": classification,
        "mode": permissions.get("mode"),
    }
''',
    },
]