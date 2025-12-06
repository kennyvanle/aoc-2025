"""Advent of Code 2025 - Day 04."""

from aoc.utils import read_input


def part1(data: str) -> int:
    """Solve part 1 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 1.
    """
    rows = data.splitlines()
    columns = len(rows[0])
    dataMap = [list(row) for row in rows]

    valid = 0
    for row_idx, row in enumerate(rows):
        for col_idx in range(columns):
            if dataMap[row_idx][col_idx] == '@':
                if checkSurroundings(dataMap, row_idx, col_idx):
                    valid += 1
    return valid

def checkSurroundings(dataMap, row, col) -> bool:
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(dataMap) and 0 <= c < len(dataMap[0]):
            if dataMap[r][c] == '@':
                count += 1
                if count >= 4:
                  return False
    return True

def part2(data: str) -> int:
    """Solve part 2 of the puzzle.

    Args:
        data: The puzzle input.

    Returns:
        The solution to part 2.
    """
    rows = data.splitlines()
    dataMap = [list(row) for row in rows]

    valid = 0
    validRolls, updatedMap = getValidRolls(dataMap)
    while validRolls > 0:
        valid += validRolls
        validRolls, updatedMap = getValidRolls(updatedMap)
        
    return valid

def getValidRolls(dataMap: list[list[str]]) -> tuple[int, list[list[str]]]:
    validRolls = 0
    clone = [list(row) for row in dataMap] 
    for r in range(len(dataMap)):
        for c in range(len(dataMap[r])):
            if dataMap[r][c] == '@' and checkSurroundings(dataMap, r, c):
                validRolls += 1
                clone[r][c] = '.'
    return validRolls, clone

if __name__ == "__main__":
    data = read_input(4)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
