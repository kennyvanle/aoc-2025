#!/usr/bin/env python3
"""Run a specific day's Advent of Code solution."""

import argparse
import importlib
import sys


def main() -> None:
    """Run the specified day's solution."""
    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2025 solutions"
    )
    parser.add_argument(
        "day",
        type=int,
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

    try:
        module = importlib.import_module(f"aoc.day{args.day:02d}")
    except ModuleNotFoundError:
        print(f"Error: Day {args.day} module not found", file=sys.stderr)
        sys.exit(1)

    from aoc.utils import read_input

    try:
        data = read_input(args.day)
    except FileNotFoundError:
        print(f"Error: Input file for day {args.day} not found", file=sys.stderr)
        sys.exit(1)

    if args.part is None or args.part == 1:
        print(f"Part 1: {module.part1(data)}")
    if args.part is None or args.part == 2:
        print(f"Part 2: {module.part2(data)}")


if __name__ == "__main__":
    main()
