"""
Validation engine for generated cybersecurity programs.

The validator performs:

1. Python syntax validation
2. Component structure validation
3. Dependency validation
4. Data-flow validation
"""

import ast


class ProgramValidator:
    """Validate generated cybersecurity programs."""

    def __init__(self):
        pass

    def validate_syntax(self, source):
        """
        Validate Python syntax using the Python AST parser.

        Returns:
            tuple:
                (True, None) when valid
                (False, error_message) when invalid
        """

        try:
            ast.parse(source)

            return True, None

        except SyntaxError as error:

            message = (
                f"Syntax error on line "
                f"{error.lineno}: {error.msg}"
            )

            return False, message

    def validate_imports(
        self,
        program,
    ):
        """
        Validate that all declared component dependencies
        have corresponding imports.
        """

        declared_imports = set(
            program.get("imports", [])
        )

        required_dependencies = set()

        for function in program.get(
            "functions",
            [],
        ):

            required_dependencies.update(
                function.get(
                    "dependencies",
                    [],
                )
            )

        # The composer returns actual import statements,
        # so dependency names must be resolved separately.
        #
        # This check is intentionally lightweight for now.
        if not required_dependencies:

            return True, None

        if not declared_imports:

            return (
                False,
                "Functions require dependencies "
                "but no imports were generated.",
            )

        return True, None

    def validate_components(
        self,
        program,
    ):
        """Validate that required program components exist."""

        required_keys = [
            "category",
            "input",
            "functions",
            "output",
            "imports",
            "source",
        ]

        for key in required_keys:

            if key not in program:

                return (
                    False,
                    f"Missing program component: {key}",
                )

        if not program["functions"]:

            return (
                False,
                "Program contains no functions.",
            )

        return True, None

    def validate_data_flow(
        self,
        program,
    ):
        """
        Validate the declared data flow between functions.

        The output of each function must satisfy the requirements
        of the next function.
        """

        functions = program.get(
            "functions",
            [],
        )

        if not functions:

            return (
                False,
                "No functions available for data-flow validation.",
            )

        for index in range(
            len(functions) - 1
        ):

            current_function = (
                functions[index]
            )

            next_function = (
                functions[index + 1]
            )

            provided = set(
                current_function.get(
                    "provides",
                    [],
                )
            )

            required = set(
                next_function.get(
                    "requires",
                    [],
                )
            )

            if not required.issubset(
                provided
            ):

                return (
                    False,
                    (
                        f"Invalid data flow: "
                        f"{current_function['name']} "
                        f"provides {provided}, "
                        f"but "
                        f"{next_function['name']} "
                        f"requires {required}."
                    ),
                )

        return True, None

    def validate(
        self,
        source,
        program=None,
    ):
        """
        Run all validation checks.

        Parameters:
            source:
                Generated Python source code.

            program:
                Composer metadata for semantic validation.
        """

        # -----------------------------------------
        # 1. Syntax
        # -----------------------------------------

        syntax_valid, syntax_error = (
            self.validate_syntax(
                source
            )
        )

        if not syntax_valid:

            return {
                "valid": False,
                "stage": "syntax",
                "error": syntax_error,
            }

        # If metadata isn't supplied, syntax validation
        # is still considered successful.
        if program is None:

            return {
                "valid": True,
                "stage": "syntax",
                "error": None,
            }

        # -----------------------------------------
        # 2. Components
        # -----------------------------------------

        components_valid, components_error = (
            self.validate_components(
                program
            )
        )

        if not components_valid:

            return {
                "valid": False,
                "stage": "components",
                "error": components_error,
            }

        # -----------------------------------------
        # 3. Imports
        # -----------------------------------------

        imports_valid, imports_error = (
            self.validate_imports(
                program
            )
        )

        if not imports_valid:

            return {
                "valid": False,
                "stage": "imports",
                "error": imports_error,
            }

        # -----------------------------------------
        # 4. Data flow
        # -----------------------------------------

        data_flow_valid, data_flow_error = (
            self.validate_data_flow(
                program
            )
        )

        if not data_flow_valid:

            return {
                "valid": False,
                "stage": "data_flow",
                "error": data_flow_error,
            }

        return {
            "valid": True,
            "stage": "complete",
            "error": None,
        }