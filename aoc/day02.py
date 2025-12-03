"""Advent of Code 2025 - Day 02."""

from aoc.utils import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 1.
    """
    ranges = data.split(",")
    sum = 0
    for r in ranges:
        start, end = map(str, r.split("-"))
        for num in range(int(start), int(end) + 1):
            if isRepeating(str(num)):
                sum += num
    return sum

def isRepeating(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 2.
    """
    ranges = data.split(",")
    sum = 0
    for r in ranges:
        start, end = map(str, r.split("-"))
        for num in range(int(start), int(end) + 1):
            if isAnyRepeating(str(num)):
                sum += num
    return sum

def isAnyRepeating(s: str) -> bool:
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            times = length // size
            if s[:size] * times == s:
                return True


if __name__ == "__main__":
    data = read_input(2)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
