"""Tests for Advent of Code 2025 - Day 04."""

import pytest

from aoc.day04 import part1, part2


class TestDay:
    """Tests for Day 04 solutions."""

    def test_part1_example(self) -> None:
        """Test part1 with example input."""
        example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        assert part1(example_input) == 13

    def test_part2_example(self) -> None:
        """Test part2 with example input."""
        example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        assert part2(example_input) == 43
