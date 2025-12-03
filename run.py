#!/usr/bin/env python3
"""Run a specific day's Advent of Code solution."""

import argparse
import importlib
import sys
import os
import requests
from dotenv import load_dotenv

def fetch_input(day: int, input_path: str) -> None:
    """Fetch input for the given day from Advent of Code and save it to the file."""
    print(f"Fetching input for day {day}...")
    session_cookie = os.getenv("AOC_SESSION")
    if not session_cookie:
        print("Error: AOC_SESSION environment variable not set", file=sys.stderr)
        sys.exit(1)

    url = f"https://adventofcode.com/2025/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(input_path, "w") as f:
            f.write(response.text.strip())
        print(f"Input for day {day} saved to {input_path}")
    else:
        print(f"Error: Failed to fetch input for day {day} (status code: {response.status_code})", file=sys.stderr)
        sys.exit(1)

def ensure_input(day: int) -> str:
    """Ensure the input file exists and is populated."""
    input_path = f"inputs/day{day:02d}.txt"
    if not os.path.exists(input_path) or os.path.getsize(input_path) == 0:
        fetch_input(day, input_path)
    return input_path

def main() -> None:
    """Run the specified day's solution."""
    load_dotenv()
    session_cookie = os.getenv("AOC_SESSION")
    if not session_cookie:
        print("Error: AOC_SESSION environment variable not set", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2025 solutions"
    )
    parser.add_argument(
        "day",
        type=int,  # Parse day as an integer
        choices=range(1, 26),
        metavar="DAY",
        help="Day to run (1-25)",
    )
    parser.add_argument(
        "-p",
        "--part",
        type=int,
        choices=[1, 2],
        help="Run only part 1 or 2 (default: both)",
    )

    args = parser.parse_args()
    day_module = f"aoc.day{args.day:02d}"  # Correctly format the module name

    try:
        module = importlib.import_module(day_module)  # Use the formatted module name
    except ModuleNotFoundError:
        print(f"Error: Day {args.day} module not found", file=sys.stderr)
        sys.exit(1)

    from aoc.utils import read_input

    # Ensure input is fetched only after confirming the module exists
    input_path = ensure_input(args.day)  # Pass args.day directly as an integer

    try:
        data = read_input(input_path)
    except FileNotFoundError:
        print(f"Error: Input file for day {args.day} not found", file=sys.stderr)
        sys.exit(1)

    if args.part is None or args.part == 1:
        print(f"Part 1: {module.part1(data)}")
    if args.part is None or args.part == 2:
        print(f"Part 2: {module.part2(data)}")

if __name__ == "__main__":
    main()