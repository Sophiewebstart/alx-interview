#!/usr/bin/python3

"""
Defines the function island_perimeter
"""


def boundary_squares(grid, i, j):
    """this function calculates the number of boundary
    squares"""
    count = 0
    rows = len(grid)
    colmn = len(grid[0])
    if (i > 0 and grid[i-1][j] == 1):
        count += 1
    if (j > 0 and grid[i][j-1] == 1):
        count += 1
    if (i < rows-1 and grid[i+1][j] == 1):
        count += 1
    if (j < colmn-1 and grid[i][j+1] == 1):
        count += 1
    return count


def island_perimeter(grid):
    """this function returns the perimeter of an island
    described with grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4 - boundary_squares(grid, i, j)
    return perimeter
