class Solution:
    def coinsInALineIII(self, a):
        if not a: return 0
        n = len(a)
        if n <= 2: return max(a)
        '''
        for the first turn
        the first player has the choice to pick left or right
        he will make the decision that the minimal of his rival will make after his choice
        his rival will use the same strategy as him, which we can dynamic programming.
        use two dimension list to construct the max sum of coins by one player
        '''
        s = {}
        def helper(i, j):
            if (i, j) in s:
                return s[(i, j)]
            if i == j:
                return a[i]
            s[(i, j)] = sum(a[i:j+1]) - min(helper(i+1, j), helper(i, j-1))
            return s[(i, j)]
        return helper(0, len(a)-1) > sum(a)/2

so = Solution()
print(so.coinsInALineIII([1,2,4]))
print(so.coinsInALineIII([1,20,2]))