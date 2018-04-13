class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        s = [[int(c) for c in row] for row in matrix]  
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                s[i][j] = 0 if matrix[i][j] == "0" else min(s[i-1][j], s[i][j-1], s[i-1][j-1]) + 1
        return max([max(row) for row in s]) ** 2
s0 = Solution()
matrix = [[1,0],[0,1]]
print(s0.maximalSquare(matrix))
