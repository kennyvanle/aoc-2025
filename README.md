# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Project Structure

```
aoc2025/
├── aoc/                  # Solution modules
│   ├── __init__.py
│   ├── utils.py          # Utility functions (read_input, etc.)
│   ├── day01.py          # Day 1 solution
│   ├── day02.py          # Day 2 solution
│   └── ...               # Days 3-25
├── inputs/               # Puzzle input files
│   ├── day01.txt
│   ├── day02.txt
│   └── ...               # Days 3-25
├── tests/                # Pytest test files
│   ├── __init__.py
│   ├── test_day01.py
│   ├── test_day02.py
│   └── ...               # Days 3-25
├── run.py                # CLI runner script
├── pyproject.toml        # Project configuration
└── README.md
```

## Installation

```bash
# Install the package in development mode
pip install -e ".[dev]"
```

## Usage

### Running Solutions

Run a specific day's solution:

```bash
# Run both parts for a day
python run.py 1

# Run only part 1
python run.py 1 -p 1

# Run only part 2
python run.py 1 -p 2
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific day
pytest tests/test_day01.py

# Run with verbose output
pytest -v
```

## Input Files

Place your puzzle inputs in the `inputs/` directory with the naming convention `dayXX.txt` (e.g., `day01.txt`, `day02.txt`).

## License

MIT