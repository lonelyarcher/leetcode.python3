'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        s1 = [0, nums[0]]
        s2 = [0, 0]
        
        for j in range(1, len(nums)):
            if j < len(nums) - 1:
                 s1.append(max(nums[j] + s1[-2], s1[-1]))
            s2.append(max(nums[j] + s2[-2], s2[-1]))
        return max(s1[-1], s2[-1])
so = Solution()
print(so.rob([2,3,5,2,1]))       