""" Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently? """
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len, cur_len, flipped = 0, 0, -1 # assume we have flip the -1 index, it helps to coding a lot, because we can take it granted for flipped before, then update the flipping in new position
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = i - flipped
                flipped = i
        print(max_len, cur_len)
        return max(max_len, cur_len)

s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0,])) #4
print(s.findMaxConsecutiveOnes([1,0,0,1,1,1,])) #4