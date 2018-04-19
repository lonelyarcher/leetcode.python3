'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''

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