"""
Digital forensics function components.
"""

FORENSICS_FUNCTIONS = [

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
]