"""
Automatically generated cybersecurity utility.

Category: forensics
"""




def calculate_entropy(data):
    """Calculate Shannon entropy for byte data."""
    if not data:
        return 0.0

    frequency = {}

    for byte in data:
        frequency[byte] = frequency.get(byte, 0) + 1

    entropy = 0.0
    length = len(data)

    for count in frequency.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy


def get_bytes_input():
    """Read binary data from a file."""
    file_path = input("Enter file path: ").strip()

    with open(file_path, "rb") as file:
        return file.read()


def display_success(value):
    """Display a successful result."""
    print(f"[+] {value}")


def main():
    """Run the generated cybersecurity utility."""

    input_value = get_bytes_input()

    result = calculate_entropy(input_value)

    display_success(result)


if __name__ == "__main__":
    main()
