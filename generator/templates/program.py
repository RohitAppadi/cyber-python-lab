"""
README generation utilities.
"""

from pathlib import Path


README_TEMPLATE = Path(
    "generator/templates/readme.md"
).read_text(
    encoding="utf-8"
)


def build_readme(program, program_name):
    """Build README documentation for a generated program."""

    functions = "\n".join(
        f"- `{function['name']}`"
        for function in program["functions"]
    )

    description = (
        program["functions"][0]["description"]
    )

    return README_TEMPLATE.format(
        title=program_name.replace("_", " ").title(),
        description=description,
        category=program["category"],
        difficulty="Beginner",
        input=program["input"]["name"],
        functions=functions,
        output=program["output"]["name"],
        filename=f"{program_name}.py",
    )