"""Tests for Advent of Code 2025 - Day 02."""

import pytest

from aoc.day02 import part1, part2


class TestDay:
    """Tests for Day 02 solutions."""

    def test_part1_example(self) -> None:
        """Test part1 with example input."""
        example_input = ("11-22,95-115,998-1012,1188511880-1188511890,"
                         "222220-222224,1698522-1698528,446443-446449,"
                         "38593856-38593862,565653-565659,824824821-824824827,"
                         "2121212118-2121212124")
        assert part1(example_input) == 1227775554

    def test_part2_example(self) -> None:
        """Test part2 with example input."""
        example_input = ""
        assert part2(example_input) == 0
