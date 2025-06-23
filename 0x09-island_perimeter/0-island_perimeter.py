#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]): A list representing the grid, where
                                0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    colmn = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(colmn):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
