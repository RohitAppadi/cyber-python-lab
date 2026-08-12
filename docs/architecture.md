# Architecture

## 1. System Overview

Cyber Python Lab is organized as a pipeline rather than a single generator function.

```text
                    Component Registry
                           |
          +----------------+----------------+
          |                |                |
        Inputs          Functions         Outputs
          |                |                |
          +----------------+----------------+
                           |
                           v
                 Program Composer
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
                    +------+------+
                    |             |
                  .py           README
                    |             |
                    +------+------+
                           |
                           v
                    GitHub Actions
```

## 2. Component Layer

The component layer contains reusable building blocks.

### Inputs

Input components collect or define the initial data required by a program.

Examples include:

- Hostname
- IP address
- Network
- URL
- File path
- Text

### Functions

Function components perform the actual cybersecurity-oriented operations.

Every function declares:

```text
name
category
requires
provides
dependencies
code
```

### Outputs

Output components convert the final result into a user-facing representation.

This separation keeps input collection and result presentation independent from processing logic.

## 3. Dependency Model

The composer uses explicit data contracts.

A function may declare:

```text
requires: hostname
provides: ip_address
```

Another function may declare:

```text
requires: ip_address
provides: ip_information
```

The composer can then form:

```text
hostname
    |
    v
resolve_hostname
    |
    v
ip_address
    |
    v
analyze_ip
    |
    v
ip_information
```

The important property is that the graph is validated before the source is assembled.

## 4. Program Composer

The composer is responsible for:

1. Selecting functions belonging to the requested category.
2. Finding compatible input components.
3. Selecting a valid starting function.
4. Tracking currently available data types.
5. Finding subsequent compatible functions.
6. Preventing repeated functions in the same chain.
7. Collecting required dependencies.
8. Selecting a compatible output.
9. Passing the resulting components to the source builder.

The composer therefore acts as the central planning layer.

## 5. Import Resolution

Functions declare their dependencies by name.

For example:

```text
dependencies:
    hashlib
```

The import registry maps that dependency to actual source:

```python
import hashlib
```

The composer resolves the required imports and removes duplicates before inserting them into the generated source.

This avoids embedding import-management logic inside every component.

## 6. Source Construction

The source builder assembles:

```text
module documentation
        +
imports
        +
function definitions
        +
input function
        +
output function
        +
main()
```

The generated program follows a consistent structure even though the internal function chain changes.

## 7. Validation Layer

Validation is deliberately placed after source construction.

The generated program is not accepted simply because a composition was found.

The system checks the resulting source and rejects invalid output.

The project distinguishes between:

- Syntax failures
- Semantic failures

This distinction makes failures easier to diagnose.

## 8. Deduplication Layer

The deduplicator computes a fingerprint for generated source.

If the fingerprint already exists, the composition is considered a duplicate and another generation attempt can be made.

This allows randomness to remain part of the system without allowing the repository to fill with identical programs.

## 9. Artifact Generation

Once a program passes validation and uniqueness checks, the artifact generator creates a dedicated directory:

```text
programs/
└── category/
    └── program_name/
        ├── program_name.py
        └── README.md
```

This makes every generated utility a self-contained learning artifact.

## 10. Automation Layer

GitHub Actions is the outermost layer.

The workflow can be triggered manually or by schedule.

The intended sequence is:

```text
GitHub trigger
      |
      v
Checkout
      |
      v
Python environment
      |
      v
Generator
      |
      v
Validation
      |
      v
Artifact creation
      |
      v
Git commit
      |
      v
Git push
```

The automation layer does not contain generation logic. It simply executes the existing generator and publishes the resulting artifacts.

## 11. Architectural Principle

The architecture intentionally separates concerns:

```text
Components      What can be done
Composer        What can be connected
Builder         How code is assembled
Validator       Whether code is acceptable
Deduplicator    Whether code is new
Generator       Where artifacts are stored
GitHub Actions  When the process runs
```

This makes each part independently expandable.

## 12. Current Architectural Limitation

The current graph is still relatively small.

The latest stress test produced:

```text
1 function : 42
2 functions: 51
3 functions: 5
4 functions: 2
```

This shows that the composer supports deeper chains, but most available combinations are still one or two functions long.

The next architectural improvement is therefore not a complete rewrite. It is expansion of the component graph and improvement of the path-selection strategy.

![Latest architecture stress-test evidence](images/stress-test-latest.png)
