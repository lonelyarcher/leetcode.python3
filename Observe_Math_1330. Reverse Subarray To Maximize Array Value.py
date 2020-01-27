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

'''
Observe the example:
1. only the start and end of subarray matters, the diff inside subarray will not change after reverse.
2. ...[a, b]...[c, d].... let's say, we reverse subarray [b, ..., c], so the effect will be abs(a - c) + abs(b - d) - abs(a - b) - abs(c - d)
3. if [a,b] and [c,d] not overlap, (if overlap, reverse will not increase answer), 
then answer will increase by 2 * gap, gap = min(c, d) - max(a, b) if a, b < c, d, vice versa
so we go through the pairs (python zip() is good at it), maintain max_start and min_end, 2 * the gap between them will be our best increasement after reverse
4. the nums[0] and nums[-1] are special, because the left of start and right of end will not count, we can calculate to additional for swap with head and tail
5. we can do all maintainance in one loop. 
'''

from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int] ) -> int:
        n = len(nums)
        base = sum(abs(nums[i] - nums[i + 1]) for i in range(n -1))
        max_start, min_end, swap = -float('inf'), float('inf'), 0
        for a, b in zip(nums, nums[1:]):
            swap = max(swap, abs(b - nums[0]) - abs(a - b), abs(a - nums[-1]) - abs(a - b)) # maintain the increasement with swap head and tail
            max_start = max(max_start, min(a, b))
            min_end = min(min_end, max(a, b))    
        return max(2 * max(0, max_start - min_end), swap) + base
print(Solution().maxValueAfterReverse([2,5,1,3,4])) # 11  
print(Solution().maxValueAfterReverse([2,3,1,5,4])) # 10    
print(Solution().maxValueAfterReverse([2,4,9,24,2,1,10])) # 68