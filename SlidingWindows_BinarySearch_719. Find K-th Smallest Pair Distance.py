""" Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2. """

'''
k-th problem, we can consider binary search on all possible distance, if we find first target which the number of distances le to target >= K, then the target is answer.
Sliding windows to count the smaller distances:
keep moving the fast pointer r in a for loop, for each r, move the l from left end until nums[r] - nums[l] <= target, then ans += r - l  

the time complexity O(n*log(n) + n*log(1000000))
'''

from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        def possible(target):
            l = ans = 0
            for r in range(len(nums)):  # sliding window, keep faster pointer in for loop, then shrink another slow pointer to maintain valid
                while r > l and nums[r] - nums[l] > target:
                    l += 1
                ans += r - l
            return ans >= k
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l
        
print(Solution().smallestDistancePair([38,33,57,65,13,2,86,75,4,56], 26)) # 36
print(Solution().smallestDistancePair([2,2,0,1,1,0,0,1,2,0], 2)) # 0
print(Solution().smallestDistancePair(nums = [1,3,1], k = 1)) # 0
print(Solution().smallestDistancePair(nums = [62,100,4], k = 2)) # 58



