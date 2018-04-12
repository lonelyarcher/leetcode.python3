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
        dp =[0, nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[-1], nums[i] + dp[-2]))
        return dp[-1]

    def rob2(self, nums): # use prev and prev of prev to replace dp list, save space
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        pre2, pre = 0, nums[0]
        for i in range(1, len(nums)):
            cur = max(pre, nums[i] + pre2)
            pre2 = pre
            pre = cur
        return pre
   
so = Solution()
print(so.rob([2,3,5,2,1]))