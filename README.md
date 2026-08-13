# Cyber Python Lab

Cyber Python Lab is a component-driven Python program generation engine designed for cybersecurity learning, experimentation, and automation.

The project generates complete Python cybersecurity utilities by composing reusable components according to their declared dependencies, input requirements, and output data types.

Rather than generating arbitrary source code, the system uses a controlled composition model based on:

`requires → provides`

This allows the generator to create different programs while maintaining compatibility between processing stages.

---

## Project Overview

Cyber Python Lab explores how software components can be automatically composed into functional cybersecurity utilities.

Each function component declares:

- The cybersecurity category it belongs to
- The type of data it requires
- The type of data it provides
- The Python dependencies it needs
- The source code used during generation

The composition engine uses these declarations to construct compatible processing chains.

For example:

```text
Hostname
   ↓
Resolve Hostname
   ↓
IP Address
   ↓
Analyze IP
   ↓
IP Information
```

The resulting chain is assembled into a standalone Python program and accompanied by its own README.

---

## Core Features

### Dependency-Aware Program Composition

Functions are not selected completely at random.

The composer tracks the data currently available in the program and only selects functions whose requirements can be satisfied.

```text
Input
  ↓
Compatible Function
  ↓
New Data
  ↓
Compatible Function
  ↓
Output
```

This provides controlled randomness while preventing incompatible function combinations.

### Component-Based Architecture

Cybersecurity functions are organized by category:

```text
generator/
├── categories/
│   ├── cryptography.py
│   ├── forensics.py
│   ├── network.py
│   ├── system_security.py
│   └── web_security.py
│
├── components/
│   ├── functions.py
│   ├── imports.py
│   ├── inputs.py
│   ├── logic.py
│   └── outputs.py
│
└── engine/
```

The category modules contain the actual function registries, while `components/functions.py` aggregates them into the `FUNCTION_COMPONENTS` collection consumed by the composer.

This separation keeps individual cybersecurity domains easier to maintain and debug.

### Multiple Cybersecurity Domains

The current generator supports:

- Cryptography
- Digital forensics
- Network security
- System security
- Web security

The component library currently includes functionality such as:

- SHA-256 hashing
- Base64 encoding and decoding
- Shannon entropy calculation
- File hashing
- File size analysis
- IP validation
- IP classification
- Subnet calculation
- Hostname resolution
- Domain extraction
- URL extraction
- File permission inspection

---

## Generation Pipeline

A generated program passes through several stages:

```text
Component Registry
        ↓
Program Composer
        ↓
Dependency Resolution
        ↓
Source Construction
        ↓
Validation
        ↓
Deduplication
        ↓
Artifact Generation
```

Each stage has a separate responsibility.

### 1. Component Registry

Stores reusable cybersecurity components and their metadata.

### 2. Program Composer

Selects compatible inputs and functions and constructs a processing chain.

### 3. Dependency Resolution

Determines which Python imports are required by the selected components.

### 4. Source Construction

Combines imports, functions, input handling, processing logic, and output handling into a complete Python program.

### 5. Validation

Checks the generated source before it is accepted.

### 6. Deduplication

Prevents previously generated compositions from being treated as new programs.

### 7. Artifact Generation

Creates a dedicated directory containing:

```text
program.py
README.md
```

for every accepted program.

---

## Architecture

The project follows a layered architecture:

```text
                    Component Registry
                           |
                           v
                  Dependency Composer
                           |
                           v
                    Source Builder
                           |
                           v
                       Validator
                           |
                           v
                     Deduplicator
                           |
                           v
                  Artifact Generator
                           |
                           v
                  Generated Programs
```

The architecture deliberately separates:

| Layer | Responsibility |
| --- | --- |
| Categories | Organize cybersecurity function components |
| Components | Aggregate inputs, outputs, imports, and functions |
| Composer | Build compatible function chains |
| Validator | Verify generated programs |
| Deduplicator | Detect previously generated programs |
| Generator | Create program artifacts |
| GitHub Actions | Automate execution and publication |

---

## Function Contracts

The central design principle is the explicit declaration of data dependencies.

A component can declare:

```python
"requires": ["hostname"],
"provides": ["ip_address"]
```

Another component can declare:

```python
"requires": ["ip_address"],
"provides": ["ip_information"]
```

The composer can therefore connect them automatically.

This creates a small data-flow graph:

```text
hostname
   ↓
resolve_hostname
   ↓
ip_address
   ↓
analyze_ip
   ↓
ip_information
```

This approach separates two important concerns:

```text
Syntax correctness
        ≠
Logical compatibility
```

A program must satisfy both.

---

## Generated Program Structure

Each generated program is stored independently:

```text
programs/
└── <category>/
    └── <program-name>/
        ├── <program-name>.py
        └── README.md
```

This makes generated utilities independently readable, testable, and reusable.

The generated README explains the purpose and usage of the individual program.

---

## Validation and Reliability

The generator does not consider a program successful merely because a composition was found.

Generated programs pass through validation before being written as final artifacts.

The development process also introduced stress testing to evaluate the generator across many consecutive compositions.

A representative 100-program stress test achieved:

```text
Generated successfully : 100
Composition failures   : 0
Syntax failures        : 0
Semantic failures      : 0
```

The same testing process also measures duplicate generation and chain length to identify limitations in the component graph.

The system has demonstrated generation chains ranging from one to four functions.

---

## Engineering Challenges

The project evolved through several engineering problems rather than being designed perfectly from the beginning.

### Dependency Compatibility

Randomly selecting functions can produce incompatible data flows.

The `requires` and `provides` model was introduced to constrain function selection.

### Source Assembly

Generated source must correctly combine imports, function definitions, input handling, processing logic, and output handling.

The source builder centralizes this responsibility.

### Duplicate Generation

A finite component graph naturally produces repeated compositions.

Deduplication was therefore introduced as a separate stage.

### Component Maintainability

The initial function registry contained all cybersecurity components in a single large file.

As the registry grew, debugging and maintenance became increasingly difficult.

The function library was refactored into category-specific modules while preserving the existing `FUNCTION_COMPONENTS` interface used by the composer.

### File-System Conflicts

Generated programs require unique directories to prevent one generated artifact from overwriting another.

Program naming therefore incorporates unique identifiers when necessary.

---

## Automation

The project is designed to work with GitHub Actions for automated program generation.

The intended workflow is:

```text
GitHub Actions Trigger
        ↓
Checkout Repository
        ↓
Set Up Python
        ↓
Compile Generator
        ↓
Generate Program
        ↓
Validate Program
        ↓
Create Artifact
        ↓
Commit Generated Program
        ↓
Push to Repository
```

This allows the repository to act as a continuously expanding collection of generated cybersecurity utilities.

---

## Project Structure

```text
cyber-python-lab/
│
├── .github/
│   └── workflows/
│
├── generator/
│   ├── categories/
│   │   ├── cryptography.py
│   │   ├── forensics.py
│   │   ├── network.py
│   │   ├── system_security.py
│   │   └── web_security.py
│   │
│   ├── components/
│   │   ├── functions.py
│   │   ├── imports.py
│   │   ├── inputs.py
│   │   ├── logic.py
│   │   └── outputs.py
│   │
│   ├── engine/
│   │   └── composer.py
│   │
│   └── main.py
│
├── programs/
│
├── docs/
│   ├── architecture.md
│   ├── engineering-journal.md
│   ├── learning.md
│   └── project-overview.md
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Running the Generator

Clone the repository and navigate to the project directory.

Run:

```bash
python -m generator.main
```

The generator selects a cybersecurity category, composes a compatible program, validates the result, checks for duplicates, and creates the resulting artifact.

Generated programs are placed under:

```text
programs/
```

---

## Development Verification

The generator can be checked for Python syntax errors with:

```bash
python -m compileall generator
```

The generator itself can then be executed with:

```bash
python -m generator.main
```

---

## Design Philosophy

Cyber Python Lab is intentionally built around constrained generation.

The goal is not maximum randomness.

The goal is:

```text
Reusable Components
        +
Explicit Contracts
        +
Controlled Randomness
        +
Validation
        +
Deduplication
        +
Automation
```

This produces a system where generated programs are both varied and constrained by the architecture of the component graph.

---

## Future Improvements

The current system provides a foundation for further development.

Potential improvements include:

- Increasing the size of the component graph
- Supporting deeper composition chains
- Improving composition diversity
- Reducing duplicate generation
- Adding richer program metadata
- Expanding validation coverage
- Adding more cybersecurity domains
- Improving generation statistics
- Expanding automated CI/CD workflows
- Adding more sophisticated dependency resolution

The primary direction is to increase the number of meaningful compositions without sacrificing compatibility or reliability.

---

## What This Project Demonstrates

Cyber Python Lab demonstrates practical experience with:

- Python package architecture
- Component-based software design
- Dependency-aware program composition
- Automated source generation
- Data-flow modeling
- Input/output abstraction
- Validation pipelines
- Deduplication strategies
- File-system automation
- Git and GitHub workflows
- GitHub Actions
- Software testing and stress testing
- Technical documentation

The project is intended not simply as a collection of generated scripts, but as an exploration of how reliable software systems can automatically construct other software from well-defined components.

---

## Author

**Rohit Appadi**

B.Tech Cybersecurity and Blockchain Technology with IoT

Interested in cybersecurity engineering, automation, Python development, and building practical security-oriented systems.
