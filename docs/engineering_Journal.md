# Engineering Journal

## Entry 01 — Initial Concept

The original objective was simple: create a system that could automatically add cybersecurity Python programs to a GitHub repository.

The first design question was how to generate programs without requiring an external language model for every run.

The decision was to build a local component library and compose programs from it.

This created a clear engineering constraint:

> The generator must create programs from known components rather than inventing arbitrary source code.

## Entry 02 — Component Registry

The first major architectural step was the creation of component registries for:

- Functions
- Imports
- Inputs
- Outputs

The function registry became the core of the system.

Each component gained metadata describing its category, dependencies, and data contracts.

## Entry 03 — Dependency-Aware Composition

A simple random function selector was not sufficient.

A randomly selected function could require data that the previous function did not produce.

The composer was therefore redesigned around:

```text
requires -> provides
```

The system tracks the data currently available in the chain and only selects functions whose requirements can be satisfied.

This was the point where the project changed from a random script generator into a constrained composition engine.

## Entry 04 — Source Generation Problems

Generated source initially exposed several issues:

- Incorrect indentation
- Function-name extraction problems
- Invalid regular expressions
- Incorrect output calls
- Null-byte corruption during an intermediate generation attempt

These failures were useful because they exposed the difference between component correctness and complete-program correctness.

The source builder was tightened so that function definitions, input functions, output functions, and `main()` were assembled consistently.

## Entry 05 — File-System Reliability

The artifact generator initially attempted to create a directory that already existed.

This resulted in Windows file-system errors.

The solution was to make generated program directories unique, including a short identifier when necessary.

The resulting structure became:

```text
programs/
└── network/
    └── calculate_subnet_<identifier>/
```

This prevents a new generation from overwriting an earlier artifact.

## Entry 06 — Validation

The generator was then connected to validation.

A program was no longer considered successful merely because composition succeeded.

The pipeline became:

```text
compose
  |
  v
build source
  |
  v
validate
```

The validation stage became one of the most important reliability boundaries in the project.

## Entry 07 — Deduplication

Repeated generation revealed another problem: random selection frequently produced the same program.

A deduplication layer was introduced.

This turned duplicate generation from an invisible problem into a measurable metric.

The stress test reports duplicate counts so that the effect of future component expansion can be measured.

## Entry 08 — Component Graph Expansion

The component library was expanded across five cybersecurity domains:

- Cryptography
- Forensics
- Network
- System security
- Web security

Additional intermediate data types were introduced to create deeper paths.

Examples include:

```text
hostname
    ->
ip_address
    ->
ip_information
    ->
ip_classification
```

and:

```text
file_path
    ->
file_size
    ->
file_size_classification
```

This increased the number of possible compositions and introduced multi-stage programs.

## Entry 09 — Stress Testing

A 100-program in-memory stress test was introduced.

The test measures:

- Generation success
- Composition failures
- Syntax failures
- Semantic failures
- Duplicates
- Category distribution
- Chain depth

One recorded run produced:

```text
Generated successfully : 100
Composition failures   : 0
Syntax failures        : 0
Semantic failures      : 0
Duplicates             : 55
```

Chain distribution:

```text
1 function(s) : 42
2 function(s) : 51
3 function(s) : 5
4 function(s) : 2
```

The result demonstrated that the core pipeline was stable while also exposing the remaining limitation: the graph still favors short chains.

![Latest stress-test run](images/stress-test-latest.png)

## Entry 10 — Lessons from the Stress Test

The stress test changed how the project was evaluated.

Instead of asking:

> Does the generator work?

the more useful questions became:

- How often does composition fail?
- How often does validation fail?
- How diverse are generated programs?
- How deep are the generated chains?
- How quickly does the graph produce duplicates?

This converted development from subjective inspection into measurable engineering.

## Entry 11 — Repository Automation

The next major step was integrating GitHub Actions.

The generator is designed to run without an external LLM and can therefore execute inside a standard Python CI environment.

The workflow is responsible for:

1. Checking out the repository.
2. Setting up Python.
3. Compiling the generator.
4. Running the generator.
5. Adding generated artifacts.
6. Creating a commit.
7. Pushing the result.

This makes the repository capable of maintaining its own stream of generated cybersecurity utilities.

## Entry 12 — Current State

The project currently has a stable generation pipeline with:

```text
Component registry          Complete
Dependency-aware composer   Complete
Source generation           Complete
Validation                  Complete
Deduplication               Complete
Artifact generation         Complete
Stress testing              Complete
GitHub Actions              Integration stage
```

The next engineering focus is increasing graph depth and uniqueness rather than replacing the existing architecture.

## Engineering Principle

The project repeatedly reinforced one principle:

> A reliable generator should constrain randomness rather than eliminate it.

Randomness provides variety.

Contracts provide correctness.

Validation provides reliability.

Deduplication provides diversity.

Automation provides continuity.

Together, those layers form the foundation of Cyber Python Lab.
