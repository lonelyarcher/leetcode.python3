""" Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.

 
Constraints:

m == mat.length
n == mat[0].length
1 <= m <= 3
1 <= n <= 3
mat[i][j] is 0 or 1. """

""" since mat is at most 3 * 3, so total 9 cell, we can use 9 bit binary number to represents the state of each flip
Do a BFS to try flip each cell, find mini steps to get 0 state
"""
from functools import reduce
from typing import List
from collections import deque
class Solution:
    
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        q = deque([reduce(lambda x, y: (x << 1) + y, [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))][::-1])])
        seen = {q[0]}
        step = 0
        while q:
            l = len(q)
            for _ in range(l):
                s = q.popleft()
                if not s: return step
                for i in range(m):
                    for j in range(n):
                        cp = s
                        for ni, nj in (i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1): # expression list as tuple, the comma is optional, 'for, return, assign'  accept expression list
                            if 0 <= ni < m and 0 <= nj < n: 
                                cp ^= 1 << ni * n + nj
                        if cp not in seen:
                            q.append(cp)
                            seen.add(cp)
            step += 1
        return -1

#directly use str(list) as key in set()
    def minFlips_2(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        q = deque([mat])
        seen = {str(mat)}
        step = 0
        def flip(A, i, j):
            for ni, nj in (i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ni < m and 0 <= nj < n: 
                    A[ni][nj] ^= 1
        while q:
            l = len(q)
            for _ in range(l):
                s = q.popleft()
                if all(not any(r) for r in s): return step
                for i in range(m):
                    for j in range(n):
                        flip(s, i, j)
                        if str(s) not in seen:
                            q.append([row[:] for row in s])
                            seen.add(str(s))
                        flip(s, i, j)

            step += 1
        return -1

        
print(Solution().minFlips([[1,0,0],[1,0,0]])) #-1
print(Solution().minFlips([[1,1,1],[1,0,1],[0,0,0]])) #6
print(Solution().minFlips([[0,0],[0,1]])) #3
print(Solution().minFlips([[0]])) #0

print(Solution().minFlips_2([[1,0,0],[1,0,0]])) #-1
print(Solution().minFlips_2([[1,1,1],[1,0,1],[0,0,0]])) #6
print(Solution().minFlips_2([[0,0],[0,1]])) #3
print(Solution().minFlips_2([[0]])) #0

