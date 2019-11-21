'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on
it represented by array nums. You are asked to burst all the balloons. If the you
burst balloon i you will get nums[left] nums[i] nums[right] coins. Here left and right
are adjacent indices of i. After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
Note: (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore
you can not burst them. (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:
Given [3, 1, 5, 8]
Return 167
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167
'''
# focus the last step, [1, 8, 1] -> [1, 1]   +8, the left part including 8 are from [1, 3, 1, 5, 8]
# the right part are from [8, 1], so it could break down to two part with the edge balloon not bursted, good for dp
# dp[i, j] = max(nums[i]*nums[j]*nums[k] + dp[i,k] + dp[k, j] for k in [i+1,...,j-1]) 
# k can only be middle elements excluding left and right edges i, j
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        memo = {}
        def helper(i, j):
            if (i, j) in memo: 
                return memo[(i, j)]
            memo[(i, j)] = max( [ helper(i, k) + nums[i] * nums[k] * nums[j] + helper(k, j) for k in range(i + 1, j)], default=0 )
            return memo[i, j]
        return helper(0, len(nums) - 1)

print(Solution().maxCoins([3, 1, 5, 8]))