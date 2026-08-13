"""
Cryptography function components.
"""

CRYPTOGRAPHY_FUNCTIONS = [

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
]