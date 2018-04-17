class Solution:
    def coinsInALineII(self, a):
        if not a: return 0
        n = len(a)
        if n <= 2: return sum(a)
        # from the right to left, [n,    n-1, ..., 2,   1     ,0]
        #                         [a[0], ...          a[n-1]    ]
        s = {0: 0, 1: a[-1]}
        for i in range(2, n+1): 
            '''
            for the first turn
            the first player has the choice to pick one or two
            he will make the decision that the minimal of his rival will make after his choice
            his rival will use the same strategy as him, which we can dynamic programming.
            '''
            s[i] = sum(a[-i:]) - min(s[i-1], s[i-2])
        return s[n] > sum(a) - s[n]

    def coinsInALineII2(self, a):
        s = {}
        def helper(i):
            if i == len(a) - 1:
                return a[i]
            if i == len(a):
                return 0
            if i in s:
                return s[i]
            s[i] = sum(a[i:]) - min(helper(i+1), helper(i+2))
            return s[i]
        return helper(0) > sum(a) / 2

so = Solution()
print(so.coinsInALineII2([1,2,4]))
print(so.coinsInALineII2([1,2,2]))