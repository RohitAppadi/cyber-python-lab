"""
Dependency-aware program composition engine.

Builds cybersecurity programs by connecting components through
their declared requires/provides relationships.
"""

import random
import re

from generator.components.functions import FUNCTION_COMPONENTS
from generator.components.imports import IMPORT_COMPONENTS
from generator.components.inputs import INPUT_COMPONENTS
from generator.components.outputs import OUTPUT_COMPONENTS


class ProgramComposer:
    """Compose complete programs from compatible components."""

    def __init__(self):
        self.functions = FUNCTION_COMPONENTS
        self.imports = IMPORT_COMPONENTS
        self.inputs = INPUT_COMPONENTS
        self.outputs = OUTPUT_COMPONENTS

    def get_functions(self, category):
        """Return functions belonging to a category."""

        return [
            function
            for function in self.functions
            if function["category"] == category
        ]

    def get_inputs(self, category):
        """
        Return all available input components.

        Compatibility is determined by data types rather than
        cybersecurity category.
        """

        return self.inputs

    def find_compatible_inputs(self, function, category):
        """
        Find input components that completely satisfy the
        function's requirements.
        """

        required = set(
            function.get("requires", [])
        )

        compatible = []

        for component in self.get_inputs(category):

            provided = set(
                component.get("provides", [])
            )

            if required.issubset(provided):
                compatible.append(component)

        return compatible

    def find_compatible_functions(
        self,
        provided_data,
        category,
    ):
        """
        Find functions whose required data types are completely
        satisfied by the currently available data.
        """

        available = set(provided_data)

        candidates = []

        for function in self.get_functions(category):

            required = set(
                function.get("requires", [])
            )

            if not required:
                continue

            if required.issubset(available):
                candidates.append(function)

        return candidates

    def resolve_imports(self, dependencies):
        """Convert dependency names into unique import statements."""

        resolved = []

        for dependency in dependencies:

            for component in self.imports:

                if component["name"] == dependency:
                    resolved.append(
                        component["code"]
                    )
                    break

        return sorted(set(resolved))

    def choose_output(self, final_data):
        """Choose an output compatible with the final data type."""

        final_data = set(final_data)

        compatible = []

        for output in self.outputs:

            accepted = set(
                output.get("accepts", [])
            )

            if "any" in accepted:
                compatible.append(output)
                continue

            if final_data.intersection(accepted):
                compatible.append(output)

        if not compatible:
            raise ValueError(
                f"No compatible output found for: {final_data}"
            )

        return random.choice(compatible)

    def compose(
        self,
        category,
        max_functions=2,
    ):
        """
        Generate a complete cybersecurity program.

        The generated chain follows strict data flow:

        input
            ↓
        function 1
            ↓
        function 1 output
            ↓
        function 2
            ↓
        function 2 output
            ↓
        output
        """

        functions = self.get_functions(
            category
        )

        if not functions:
            raise ValueError(
                f"No functions available for category: {category}"
            )

        # Find functions that can actually receive
        # one of our available input components.
        valid_starts = []

        for function in functions:

            compatible_inputs = (
                self.find_compatible_inputs(
                    function,
                    category,
                )
            )

            if compatible_inputs:

                valid_starts.append(
                    (
                        function,
                        compatible_inputs,
                    )
                )

        if not valid_starts:
            raise ValueError(
                "No compatible input/function combination "
                f"for {category}"
            )

        # Select the first operation.
        first_function, compatible_inputs = random.choice(
            valid_starts
        )

        input_component = random.choice(
            compatible_inputs
        )

        selected_functions = [
            first_function
        ]

        dependencies = set(
            first_function.get(
                "dependencies",
                [],
            )
        )

        # IMPORTANT:
        # After the first function executes, only its output
        # becomes available to the next function.
        current_data = list(
            first_function.get(
                "provides",
                [],
            )
        )

        # Build additional stages.
        for _ in range(
            max_functions - 1
        ):

            candidates = (
                self.find_compatible_functions(
                    current_data,
                    category,
                )
            )

            selected_names = {
                function["name"]
                for function in selected_functions
            }

            candidates = [
                candidate
                for candidate in candidates
                if candidate["name"]
                not in selected_names
            ]

            if not candidates:
                break

            next_function = random.choice(
                candidates
            )

            selected_functions.append(
                next_function
            )

            dependencies.update(
                next_function.get(
                    "dependencies",
                    [],
                )
            )

            # Only this function's output is available
            # for the next stage.
            current_data = list(
                next_function.get(
                    "provides",
                    [],
                )
            )

        output_component = self.choose_output(
            current_data
        )

        imports = self.resolve_imports(
            dependencies
        )

        source = self.build_source(
            imports=imports,
            input_component=input_component,
            functions=selected_functions,
            output_component=output_component,
        )

        return {
            "category": category,
            "input": input_component,
            "functions": selected_functions,
            "output": output_component,
            "imports": imports,
            "source": source,
        }

    def build_source(
        self,
        imports,
        input_component,
        functions,
        output_component,
    ):
        """Assemble the final Python program."""

        import_section = "\n".join(
            imports
        )

        function_section = "\n\n".join(
            function["code"].rstrip()
            for function in functions
        )

        input_section = (
            input_component["code"].rstrip()
        )

        output_section = (
            output_component["code"].rstrip()
        )

        input_function = (
            self.extract_function_name(
                input_component["code"]
            )
        )

        output_call = (
            output_component["call"]
        )

        # First function receives the user's input.
        first_function = (
            functions[0]["name"]
        )

        processing = (
            f"result = "
            f"{first_function}(input_value)"
        )

        # Every subsequent function receives ONLY
        # the output of the previous function.
        if len(functions) > 1:

            current_variable = "result"

            for index, function in enumerate(
                functions[1:],
                start=2,
            ):

                next_variable = (
                    f"result_{index}"
                )

                processing += (
                    f"\n    {next_variable} = "
                    f"{function['name']}("
                    f"{current_variable}"
                    f")"
                )

                current_variable = (
                    next_variable
                )

            processing += (
                f"\n    result = "
                f"{current_variable}"
            )

        return f'''"""
Automatically generated cybersecurity utility.

Category: {functions[0]["category"]}
"""

{import_section}


{function_section}


{input_section}


{output_section}


def main():
    """Run the generated cybersecurity utility."""

    input_value = {input_function}()

    {processing}

    {output_call}


if __name__ == "__main__":
    main()
'''

    @staticmethod
    def extract_function_name(code):
        """Extract the first function name from component code."""

        match = re.search(
            r"^def\s+(\w+)\(",
            code,
            re.MULTILINE,
        )

        if not match:
            raise ValueError(
                "Could not determine component function name."
            )

        return match.group(1)