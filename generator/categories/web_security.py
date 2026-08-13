"""
Web security function components.
"""

WEB_SECURITY_FUNCTIONS = [

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
]