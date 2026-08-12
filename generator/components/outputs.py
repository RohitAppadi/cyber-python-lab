"""
Output components for the Cyber Python Lab generator.

Each output declares which data types it can display.
"""

OUTPUT_COMPONENTS = [
    {
        "name": "simple_output",
        "category": "general",
        "description": "Display a simple result.",
        "accepts": ["any"],
        "code": '''def display_result(value):
    """Display a result."""
    print(f"Result: {value}")
''',
        "call": "display_result(result)",
    },

    {
        "name": "success_output",
        "category": "general",
        "description": "Display a successful result.",
        "accepts": ["any"],
        "code": '''def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")
''',
        "call": "display_success(result)",
    },

    {
        "name": "warning_output",
        "category": "general",
        "description": "Display a warning result.",
        "accepts": ["any"],
        "code": '''def display_warning(value):
    """Display a warning result."""
    print(f"[!] {value}")
''',
        "call": "display_warning(result)",
    },

    {
        "name": "key_value_output",
        "category": "general",
        "description": "Display dictionary data.",
        "accepts": ["dictionary", "subnet_information", "permissions"],
        "code": '''def display_dictionary(data):
    """Display dictionary data."""
    if data is None:
        print("No data available.")
        return

    for key, value in data.items():
        print(f"{key}: {value}")
''',
        "call": "display_dictionary(result)",
    },
]