""" You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3*10^4
-10^5 <= nums[i] <= 10^5 """
from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int] ) -> int:
        n = len(nums)
        origin = sum(abs(nums[i] - nums[i + 1]) for i in range(n -1))
        max_i, min_i, n, ans = 0, 0, len(nums), 0
        for i in range(1, n):    
            d1 = abs(nums[i + 1] - nums[max_i] if i < n - 1 else 0) + abs(nums[max_i - 1] - nums[i] if max_i > 0 else 0) - abs(nums[i + 1] - nums[i] if i < n - 1 else 0) - abs(nums[max_i] - nums[max_i - 1] if max_i > 0 else 0)
            d2 = abs(nums[i + 1] - nums[min_i] if i < n - 1 else 0) + abs(nums[min_i - 1] - nums[i] if min_i > 0 else 0) - abs(nums[i + 1] - nums[i] if i < n - 1 else 0) - abs(nums[min_i] - nums[min_i - 1] if min_i > 0 else 0) 
            ans = max(ans, d1, d2)
            if nums[i] > nums[max_i]: 
                max_i = i
            elif nums[i] < nums[min_i]: 
                min_i = i
        return ans + origin
print(Solution().maxValueAfterReverse([2,5,1,3,4])) # 11  
print(Solution().maxValueAfterReverse([2,3,1,5,4])) # 10    
print(Solution().maxValueAfterReverse([2,4,9,24,2,1,10])) # 68