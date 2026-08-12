"""
Input components for the Cyber Python Lab generator.

Each input component describes the type of data it provides
to the generated program.
"""

INPUT_COMPONENTS = [
    {
        "name": "text_input",
        "category": "general",
        "description": "Request a text value from the user.",
        "provides": ["text"],
        "code": '''def get_text_input(prompt):
    """Get a text value from the user."""
    return input(prompt).strip()
''',
    },

    {
        "name": "hostname_input",
        "category": "network",
        "description": "Request a hostname or IP address.",
        "provides": ["hostname"],
        "code": '''def get_target_input():
    """Get a hostname or IP address from the user."""
    return input("Enter target hostname or IP: ").strip()
''',
    },

    {
        "name": "file_input",
        "category": "forensics",
        "description": "Request a file path from the user.",
        "provides": ["file_path"],
        "code": '''def get_file_input():
    """Get a file path from the user."""
    return input("Enter file path: ").strip()
''',
    },

    {
        "name": "algorithm_input",
        "category": "cryptography",
        "description": "Request a hashing algorithm from the user.",
        "provides": ["algorithm"],
        "code": '''def get_algorithm_input():
    """Get a hashing algorithm from the user."""
    return input(
        "Enter hashing algorithm (sha256/sha512): "
    ).strip().lower()
''',
    },

    {
        "name": "network_input",
        "category": "network",
        "description": "Request an IP network from the user.",
        "provides": ["network"],
        "code": '''def get_network_input():
    """Get an IP network from the user."""
    return input("Enter IP network (example: 192.168.1.0/24): ").strip()
''',
    },

    {
        "name": "encoded_text_input",
        "category": "cryptography",
        "description": "Request encoded text from the user.",
        "provides": ["encoded_text"],
        "code": '''def get_encoded_text_input():
    """Get encoded text from the user."""
    return input("Enter Base64 encoded text: ").strip()
''',
    },

    {
        "name": "bytes_input",
        "category": "forensics",
        "description": "Read binary data from a file.",
        "provides": ["bytes"],
        "code": '''def get_bytes_input():
    """Read binary data from a file."""
    file_path = input("Enter file path: ").strip()

    with open(file_path, "rb") as file:
        return file.read()
''',
    },
]