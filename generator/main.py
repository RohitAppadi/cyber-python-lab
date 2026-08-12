"""
Main entry point for the Cyber Python Lab generator.

Generation pipeline:

Random Category
    ↓
Composer
    ↓
Semantic Validator
    ↓
Deduplicator
    ↓
README Generator
    ↓
Program Artifact Generator
"""

import random

from generator.engine.composer import ProgramComposer
from generator.engine.validator import ProgramValidator
from generator.engine.deduplicator import ProgramDeduplicator
from generator.engine.generator import ProgramArtifactGenerator

from generator.utils.naming import generate_program_name
from generator.templates.program import build_readme


CATEGORIES = [
    "network",
    "cryptography",
    "forensics",
    "web_security",
    "system_security",
]

MAX_ATTEMPTS = 10


def generate_unique_program(
    composer,
    validator,
    deduplicator,
):
    """Generate a unique validated program."""

    for attempt in range(
        1,
        MAX_ATTEMPTS + 1,
    ):

        category = random.choice(
            CATEGORIES
        )

        print(
            f"Attempt {attempt}/{MAX_ATTEMPTS}"
        )

        print(
            f"Category: {category}"
        )

        try:

            max_functions = random.randint(
                1,
                4,
            )

            program = composer.compose(
                category=category,
                max_functions=max_functions,
            )

        except ValueError as error:

            print(
                f"⚠️ Composition failed: {error}"
            )

            continue

        validation = validator.validate(
            source=program["source"],
            program=program,
        )

        if not validation["valid"]:

            print(
                "❌ Validation failed."
            )

            print(
                f"Stage: {validation['stage']}"
            )

            print(
                f"Reason: {validation['error']}"
            )

            continue

        print(
            "✅ Program passed semantic validation."
        )

        if deduplicator.exists(
            program["source"]
        ):

            print(
                "⚠️ Duplicate detected."
            )

            continue

        print(
            "✅ Program is unique."
        )

        return program

    raise RuntimeError(
        "Unable to generate a unique program "
        f"after {MAX_ATTEMPTS} attempts."
    )


def main():
    """Generate one unique cybersecurity program."""

    composer = ProgramComposer()

    validator = ProgramValidator()

    deduplicator = ProgramDeduplicator(
        "generator/metadata/catalog.json"
    )

    artifact_generator = (
        ProgramArtifactGenerator(
            "programs"
        )
    )

    print(
        "🚀 Cyber Python Lab Generator"
    )

    print(
        "=" * 40
    )

    program = generate_unique_program(
        composer,
        validator,
        deduplicator,
    )

    category = program["category"]

    program_name = (
        generate_program_name(
            program
        )
    )

    readme = build_readme(
        program,
        program_name,
    )

    artifact = (
        artifact_generator.create_program(
            category=category,
            program_name=program_name,
            source=program["source"],
            readme=readme,
        )
    )

    metadata = {
        "name": program_name,
        "category": category,
        "input": program["input"]["name"],
        "functions": [
            function["name"]
            for function in program["functions"]
        ],
        "output": program["output"]["name"],
        "path": str(
            artifact["directory"]
        ),
    }

    deduplicator.add(
        program["source"],
        metadata,
    )

    print()
    print(
        "🎉 Program generated successfully!"
    )

    print(
        f"📁 {artifact['directory']}"
    )

    print(
        f"🐍 {artifact['python_file']}"
    )

    print(
        f"📖 {artifact['readme_file']}"
    )


if __name__ == "__main__":
    main()