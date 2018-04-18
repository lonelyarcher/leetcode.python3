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