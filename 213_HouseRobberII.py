# houses are in a cycle, the first one and last one are connected
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