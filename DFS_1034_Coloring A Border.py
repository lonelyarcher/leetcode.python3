""" Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid. """

"""  
DFS to iterate the designated connected component by the designated color
Only trick is how the identify a square is on border or not? if one of its neighbor is out of range or different color, then itself is on border
If you coloring the border color at the same time, it may mess up with the later identifying border, so we can first collect into a set and run after dfs. 
"""

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m, n, c = len(grid), len(grid[0]), grid[r0][c0]
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        seen, toBeColor = set(), set()
        def dfs(i, j):
            seen.add((i, j))
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == c:
                    if (ni, nj) not in seen: dfs(ni, nj)
                else: toBeColor.add((i, j))
        dfs(r0, c0)
        for i, j in toBeColor:
            grid[i][j] = color
        return grid