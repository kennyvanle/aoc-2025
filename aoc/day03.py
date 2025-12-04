"""Advent of Code 2025 - Day 03."""

from aoc.utils import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 1.
    """
    maxJoltage = 0
    lines = data.splitlines()
    for line in lines:
        length = len(line)
        last = line[length - 1]
        first = line[length - 2]
        for i in range(length - 3, -1, -1):
            placeholder = -1
            if line[i] >= first:
                placeholder = first
                first = line[i]
                if placeholder > last:
                    last = placeholder
        maxJoltage += int(f"{first}{last}")
    return maxJoltage


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 2.
    """
    # TODO: Implement solution
    return 0


if __name__ == "__main__":
    data = read_input(3)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
