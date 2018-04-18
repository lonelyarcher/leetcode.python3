class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        memo = {}
        def helper(i, j):
            if (i, j) in memo: return memo[(i, j)]
            memo[(i, j)] = max( [ helper(i, k) + nums[i] * nums[k] * nums[j] + helper(k, j) for k in range(i + 1, j)], default=0 )
            return memo[i, j]
        return helper(0, len(nums) - 1)

print(Solution().maxCoins([3, 1, 5, 8]))