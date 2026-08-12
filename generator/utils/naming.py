"""
Naming utilities for generated cybersecurity programs.
"""

import hashlib
import re


def slugify(text):
    """Convert text into a filesystem-friendly name."""

    text = text.lower().strip()

    text = re.sub(
        r"[^a-z0-9]+",
        "_",
        text,
    )

    return text.strip("_")


def generate_program_name(program):
    """
    Generate a unique-looking name from the program composition
    and its source code.
    """

    functions = program.get("functions", [])

    if not functions:
        base_name = "cybersecurity_utility"
    else:
        function_names = [
            function["name"]
            for function in functions
        ]

        base_name = "_".join(function_names)

    base_name = slugify(base_name)

    source = program.get("source", "")

    fingerprint = hashlib.sha256(
        source.encode("utf-8")
    ).hexdigest()[:8]

    return f"{base_name}_{fingerprint}"