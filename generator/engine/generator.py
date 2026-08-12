"""
Program artifact generator.

Creates a complete program directory containing:
- Python source code
- README documentation
"""

from pathlib import Path


class ProgramArtifactGenerator:
    """Create files for a generated cybersecurity program."""

    def __init__(self, programs_directory="programs"):
        self.programs_directory = Path(
            programs_directory
        )

    def create_program(
        self,
        category,
        program_name,
        source,
        readme,
    ):
        """
        Create a program directory containing the Python file
        and its README.
        """

        program_directory = (
            self.programs_directory
            / category
            / program_name
        )

        if program_directory.exists():
            raise FileExistsError(
                f"Program directory already exists: "
                f"{program_directory}"
            )

        program_directory.mkdir(
            parents=True,
            exist_ok=False,
        )

        python_file = (
            program_directory
            / f"{program_name}.py"
        )

        readme_file = (
            program_directory
            / "README.md"
        )

        python_file.write_text(
            source,
            encoding="utf-8",
        )

        readme_file.write_text(
            readme,
            encoding="utf-8",
        )

        return {
            "directory": program_directory,
            "python_file": python_file,
            "readme_file": readme_file,
        }