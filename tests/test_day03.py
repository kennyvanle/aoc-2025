"""Tests for Advent of Code 2025 - Day 03."""

import pytest

from aoc.day03 import part1, part2


class TestDay:
    """Tests for Day 03 solutions."""

    def test_part1_example(self) -> None:
        """Test part1 with example input."""
        example_input = """987654321111111
811111111111119
234234234234278
818181911112111
"""
        assert part1(example_input) == 357

    def test_part2_example(self) -> None:
        """Test part2 with example input."""
        example_input = """987654321111111
811111111111119
234234234234278
818181911112111
"""
        assert part2(example_input) == 3121910778619
