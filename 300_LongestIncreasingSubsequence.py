class Solution:
    def lengthOfLIS(self, nums): # DP O(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = [1]
        for i in range(1, len(nums)):
            s.append(max([s[j] + 1 for j in range(0,i) if nums[i] > nums[j]], default=1)) 
            print(s)   
        return max(s)




    def lengthOfLIS2(self, nums): # DP O(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] >= s[-1]:
                s.append(nums[i])
            else:
                j = self.binarySearch(s, nums[i])
                s[j] = nums[i]  
        return len(s)

    def binarySearch(s, x):
        start, end = 0, len(s)
        if start == end:
            return start
        if s[start] 



s = Solution()
#print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([4,10,4,3,8,9]))
