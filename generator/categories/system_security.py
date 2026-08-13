"""
System security function components.
"""

SYSTEM_SECURITY_FUNCTIONS = [

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