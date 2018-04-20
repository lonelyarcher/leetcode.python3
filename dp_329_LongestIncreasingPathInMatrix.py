'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        memo = {}
        matr = { i + 1j*j: matrix[i][j] for i in range(m) for j in range(n) }
        def dp(x):
            if x in memo: return memo[x]
            memo[x] = max([dp(x+1j**k) for k in range(4) if x+1j**k in matr and matr[x+1j**k] > matr[x]], default=0) + 1
            return memo[x]
        return max([dp(i + 1j*j) for i in range(m) for j in range(n)])

s = Solution()
print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))