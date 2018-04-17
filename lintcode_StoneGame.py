class Solution():
    def stoneGame(self, a):
        s = {}
        def helper(i, j):
            if i == j:
                return 0
            if (i, j) in s:
                return s[(i, j)]
            return sum(a[i:j + 1]) + min([helper(i, k) + helper(k + 1, j) for k in range(i, j)])

        return helper(0, len(a)-1)

so = Solution()
print(so.stoneGame([4, 1, 1, 4]))