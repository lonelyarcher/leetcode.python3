""" In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1. """


'''
first count and color all the connected components with different id
second try every cell == 0, add count of its neighbor component with different id
'''
from typing import List
import collections
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        map = {}
        m, n = len(grid), len(grid[0])
        
        def mov(i, j): 
             for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < m:
                    yield (ni, nj)

        def dfs(i, j, id):
            ans = 1
            grid[i][j] = id
            for ni, nj in mov(i, j):
                if grid[ni][nj] == 1:
                    ans += dfs(ni, nj, id)
            return ans
            
        id = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    map[id] = dfs(i, j, id)
                    id += 1
        # ans = max(map.values(), default=0) # may no 0 cells, so ans pre-set to max of count of component
        ans = map[2] if map else 0 # if all 0 then 0, if all 1 then only one component map[2]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cur = set()
                    for ni, nj in mov(i, j):
                        if grid[ni][nj] > 1:
                            cur.add(grid[ni][nj])
                    ans = max(ans, 1 + sum(map[i] for i in cur))
        return ans


print(Solution().largestIsland([[1, 0], [0, 1]])) # 3
print(Solution().largestIsland([[1, 1], [1, 0]])) # 4
print(Solution().largestIsland([[1, 1], [1, 1]])) # 4