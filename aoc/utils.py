"""Utility functions for Advent of Code 2025."""

from pathlib import Path


def read_input(input: str) -> str:
    """Read the input file for a given day.

    Args:
        input: The input file.

    Returns:
        The contents of the input file as a string.
    """
    input_path = Path(__file__).parent.parent / input 
    return input_path.read_text().strip()
