""" We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input: 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation: 
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Example 2:
Input: 
grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: 
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
 

Note:

The number of rows and columns in the grid will be in the range [1, 200].
The number of erasures will not exceed the area of the grid.
It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
An erasure may refer to a location with no brick - if it does, no bricks drop. """

'''straight forward O(m * n * len(hits)), do dfs/bfs at each hit'''
from typing import List 
import collections
class Solution_1:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def mov(i, j):
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > 0:
                    yield ni, nj
        def willDrop(i, j, id):
            ans = True
            grid[i][j] = id
            if i == 0: ans = False
            for ni, nj in mov(i, j):
                if grid[ni][nj] != id and not willDrop(ni, nj, id):
                    ans = False
            return ans
        def drop(i, j):
            grid[i][j] = 0
            ans = 1
            for ni, nj in mov(i, j):
                ans += drop(ni, nj)
            return ans
        id = 2
        for i, j in hits:
            if grid[i][j] == 0: ans.append(0)
            else:
                grid[i][j] = 0
                drops = 0
                for ni, nj in mov(i, j):
                    if grid[ni][nj] < id and willDrop(ni, nj, id):
                        drops += drop(ni, nj)
                ans.append(drops)
                id += 1
        return ans

'''
O(m*n + len(hits)) better than previous solution
UnionFind, first remove all the hitted block, do the uf, 
then in reverse order of hits, join the components, 
each time increase the size of connected (from the top) components, 
the increased amount is the ans of that hit

Trick 1: all block == 1 in the first row can connect to a virtual block m*n, so the non-falling blocks size[find(m*n)]
Trick 2: first set all hits block to 0, but some hits block are initial 0, so at this turn none falling, we'd better keep the original grid, and make a copy of A
Trick 3: we record a size[] to record connected component size, when join, add child size to parent, need be careful, if both already connected, don't update size
'''

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        A = [row[:] for row in grid]
        for i, j in hits: A[i][j] = 0
        
        def move(i, j):
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 1:
                    yield ni, nj
                
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        parent = [i for i in range(m * n + 1)]
        size = [A[i][j] for i in range(m) for j in range(n)] + [0]
        def find(i):
            if parent[i] != i: parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            if find(i) == find(j): return
            size[find(j)] += size[find(i)]
            parent[find(i)] = find(j)
            

        for j in range(n):
            if A[0][j] == 1:
                union(j, m * n)

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    for ni, nj in move(i, j):
                        union(i * n + j, ni * n + nj)
        ans = []
        for i, j in hits[::-1]:
            if grid[i][j]:
                pre = size[find(m * n)]
                A[i][j] = 1
                size[i * n + j] = 1
                if i == 0: union(i * n + j, m * n)
                for ni, nj in move(i, j):   
                    union(i * n + j, ni * n + nj)
                ans.append(max(0, size[find(m * n)] - pre - 1))
            else:
                ans.append(0)
        
        return ans[::-1]

print(Solution().hitBricks([[1,1,1],[0,1,0],[0,0,0]], [[0,2],[2,0],[0,1],[1,2]])) #[0,0,1,0]
print(Solution().hitBricks([[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]])) # [0 3 0] 
print(Solution().hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]])) #[1,0,1,0,0]
print(Solution().hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]])) #[2]
print(Solution().hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]])) # [0, 0]
                    

        