"""
Logic components for the Cyber Python Lab generator.

These components provide reusable control-flow patterns that
connect inputs, processing functions, and outputs.
"""

LOGIC_COMPONENTS = [
    {
        "name": "single_operation",
        "category": "general",
        "description": "Run one operation and store its result.",
        "requires": ["operation", "input_value"],
        "provides": ["result"],
        "code": '''result = operation(input_value)
''',
    },

    {
        "name": "conditional_result",
        "category": "general",
        "description": "Handle a result using a condition.",
        "requires": ["result"],
        "provides": ["message"],
        "code": '''if result:
    display_success("Operation completed successfully.")
else:
    display_warning("Operation could not be completed.")
''',
    },

    {
        "name": "display_if_valid",
        "category": "general",
        "description": "Display a result only when valid.",
        "requires": ["result"],
        "provides": ["message"],
        "code": '''if result is not None:
    display_result("Result", result)
else:
    display_warning("Invalid or unavailable result.")
''',
    },

    {
        "name": "iterate_items",
        "category": "general",
        "description": "Process multiple items using the same operation.",
        "requires": ["items", "operation"],
        "provides": ["results"],
        "code": '''results = []

for item in items:
    result = operation(item)
    results.append(result)
''',
    },

    {
        "name": "try_operation",
        "category": "general",
        "description": "Execute an operation with exception handling.",
        "requires": ["operation", "input_value"],
        "provides": ["result"],
        "code": '''try:
    result = operation(input_value)
except Exception as error:
    result = None
    print(f"Operation failed: {error}")
''',
    },

    {
        "name": "compare_values",
        "category": "general",
        "description": "Compare two values.",
        "requires": ["first_value", "second_value"],
        "provides": ["comparison_result"],
        "code": '''comparison_result = first_value == second_value
''',
    },

    {
        "name": "threshold_check",
        "category": "forensics",
        "description": "Compare a calculated value against a threshold.",
        "requires": ["result", "threshold"],
        "provides": ["message"],
        "code": '''if result >= threshold:
    display_warning("Value is above the configured threshold.")
else:
    display_success("Value is below the configured threshold.")
''',
    },
]