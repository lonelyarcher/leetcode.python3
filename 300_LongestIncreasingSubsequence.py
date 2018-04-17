import bisect
class Solution:
    def lengthOfLIS(self, nums): # DP O(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = []
        for i in range(0, len(nums)):
            s.append(max([s[j] + 1 for j in range(0,i) if nums[i] > nums[j]], default=1)) # default =
        return max(s)




    def lengthOfLIS2(self, nums): # greedy O(nlgn)
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s = {}
        for i in range(0, len(nums)):     
            s[self.binarySearch(s, nums[i])] = nums[i]  
        return len(s)

    def binarySearch(self, s, x): # bisect.bisect_left(s, x)
        '''
        find insert position, remember:
        l, r = -1, len() 
        while r - l > 1
        if mid >= target
        return r
        '''
        l,r = -1, len(s)
        while r - l  > 1:
            mid = l + (r - l) // 2
            if s[mid] == x:
                return mid
            elif s[mid] > x:
                r = mid
            else:
                l = mid
        return r




s = Solution()
print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS2([4,10,4,3,8,9]))
print(s.lengthOfLIS2([]))
print(s.lengthOfLIS2(None))