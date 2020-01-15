""" Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. 
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted. """


'''
Straight Forward to try all possible length from k to N will fail TLE O(n^2)
It has to be O(n*logn) solution, conside binary search for possible average value that can find subarray length >= k with this average value.
Why? because if we know the average, we can substract all the element with this average value, then just find a subarray sum >= 0 which can be solved in linear time
why zero, because we want transform the problem to subarray sum, if average is zero, whatever length of subarray sum will be zero too
find subarray sum >= 0 and length >= k, we can use presum and slide window to get, if we move the window for k to right, 
when we find the presum[r] - min(presum(l) where l <= r - k), then return True

'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        def subsumzero(average):
            arr = [num - average for num in nums]
            presum = [0]
            for i in range(n): presum.append(presum[-1] + arr[i])
            min_left = 0
            for i in range(k, n + 1):
                min_left = min(min_left, presum[i - k])
                if presum[i] >= min_left: return True
            return False
        l, r = min(nums), max(nums)
        while l + 0.00001 < r:
            mid = (l + r) / 2.0
            if subsumzero(mid):
                l = mid
            else:
                r = mid
        return l


print(Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4)) # 12.75