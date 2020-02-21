""" Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9 """

'''
simulation in reverse order, last number must be the largest one in target array as top, so top = (rest := sum - top) + pre, pre = top - rest
replace top with pre, we can use a heap to find max value in log(n) time.
when you get pre < 1, which means it is invalid, then return false
when you get top == 1, which means all other are 1, then return true
It is still not enough for test case [1, 1000000000] which will TLE
let's optimize: pre = top - rest
if top >> rest, so every time you are substract rest from top, like [3, 10] => [3, 7] => [3, 4] => [3, 1], so we can directly [3, 10] => [3, 10 % 3]
if rest == 1, return True
if rest == 0 or top % rest == 0 , return false

'''

from typing import List
import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            top = -heapq.heappop(heap)
            rest = total - top
            if top == 1 or rest == 1:
                return True
            pre = top - rest
            if pre <= 0 or rest == 0 or top % rest == 0 : return False
            pre = top % rest
            heapq.heappush(heap, -pre)
            total = pre + rest
        return False
print(Solution().isPossible([9,3,5])) # true
print(Solution().isPossible([1,1,1,2])) # false
print(Solution().isPossible([8,5])) # true
