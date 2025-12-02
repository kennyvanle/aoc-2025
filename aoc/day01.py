"""Advent of Code 2025 - Day 01."""

from aoc.utils import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 1.
    """
    curr = 50
    lines = data.splitlines()
    count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            curr = (curr - distance) % 100
        elif direction == "R":
            curr = (curr + distance) % 100
        if curr == 0:
            count += 1
    return count


def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 2.
    """
    curr = 50
    lines = data.splitlines()
    count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        for i in range(distance):
            if direction == "L":
                curr = (curr - 1) % 100
            elif direction == "R":
                curr = (curr + 1) % 100
            if curr == 0:
                count += 1
    return count

if __name__ == "__main__":
    data = read_input(1)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
