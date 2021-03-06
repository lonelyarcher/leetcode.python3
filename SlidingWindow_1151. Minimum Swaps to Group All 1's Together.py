""" 
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
 

Note:

1 <= data.length <= 10^5
0 <= data[i] <= 1 """

'''
first find out how many one in the array an length, then moving this fix_length windows sliding from left to right
'''
from collections import Counter
from typing import List
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = Counter(data)[1]
        zeros = Counter(data[:ones])[0]
        minSwap = zeros
        for i in range(ones, len(data)):
            if data[i] == 0: zeros += 1
            if data[i - ones] == 0: zeros -= 1
            minSwap = min(zeros, minSwap)
        return minSwap