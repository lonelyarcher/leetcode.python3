'''
You are given a map in form of a two-dimensional integer grid where 1 represents land 
and 0 represents water. Grid cells are connected horizontally/vertically 
(not diagonally). 
The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
import operator
import itertools
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        grid = {i + 1j*j: grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))}
        res = 0
        def dfs(x):
            nonlocal res
            for i in range(4):
                grid[x] = 2
                y = x + 1j**i
                if y not in grid or grid[y] == 0:                    
                    res += 1
                elif grid[y] == 1:
                    dfs(y)
        for x in grid:
            if grid[x] == 1:
                dfs(x)
        return res


    def islandPerimeter2(self, grid):
        return sum(
            sum(map(operator.ne, [0] + row, row + [0])) 
            for row in itertools.chain(iter(grid), map(list, zip(*grid)))
        ) # zip return iterator of tuple, chain can combine the iterators

    def islandPerimeter3(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        perimeter = 0
        row_up = itertools.repeat(0) # use repeat to initiate list iterator 
        for row in grid:
            val_left = 0

            for val_up, val in zip(row_up, row):
                perimeter += val != val_up
                perimeter += val != val_left
                val_left = val
            else:
                perimeter += val_left

            row_up = row
        else:
            perimeter += sum(row_up)

        return perimeter

# test
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(Solution().islandPerimeter3(grid))