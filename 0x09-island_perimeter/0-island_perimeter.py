#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid
    grid is a list of integers
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            perimeter += 4
            if i > 0:
                perimeter = perimeter - grid[i - 1][j]
            if i < len(grid) - 1:
                perimeter = perimeter - grid[i + 1][j]
            if j > 0:
                perimeter = perimeter - grid[i][j - 1]
            if j < len(grid[0]) - 1:
                perimeter = perimeter - grid[i][j + 1]
    return perimeter
