"""Utility functions for Advent of Code 2025."""

from pathlib import Path


def read_input(day: int) -> str:
    """Read the input file for a given day.

    Args:
        day: The day number (1-25).

    Returns:
        The contents of the input file as a string.
    """
    input_path = Path(__file__).parent.parent / "inputs" / f"day{day:02d}.txt"
    return input_path.read_text().strip()
