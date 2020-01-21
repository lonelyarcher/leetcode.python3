""" There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 
Example 1:

Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100 """

'''
Greedy, sort the interval (water range of each tap) by start, from the left go through every intervals
maintain two variable: current_covered and next_covered, when new start of tap is out of next_covered, return False
when out of current but inside of next, increase answer and set current to next
There is key point to skip: you actually don't need sort, because tap has order from left to right, it is possible we meet some faked gap but it will covered in later large range gap
'''

from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        cover = [(max(0, i - v), min(n, i + v)) for i, v in enumerate(ranges)]
        cover.sort()
        cover = {i: j for i, j in cover}

        if not cover: return -1
        A = sorted(cover)

        ans = 1
        coverable = covered = cover[A[0]]
        for i in range(1, len(A)):
            if A[i] <= covered:
                coverable = max(coverable, cover[A[i]])
            else:
                if A[i] > coverable: return -1
                else:
                    ans += 1
                    covered = coverable
                    coverable = max(coverable, cover[A[i]])

        if n > coverable: return -1
        if covered < n <= coverable: return ans + 1
        else: return ans

'''
Better coding, like jump game, dp[i] is from this index i, rightest index which can be cover with the same tap as this index i
'''
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] * (n + 1)
        for i, c in enumerate(ranges):
            dp[max(i - c, 0)] = max(dp[max(i - c, 0)], min(n, i + c)) # the rightest idx can be covered by the same tap
        start = end = step = 0 # jump range [start, end] by range [end, next]
        while end < n:
            step += 1
            start, end = end, max(dp[i] for i in range(start, end + 1))
            if start == end: return -1 # if can't make any progress, then means there must be a gap after this end, return -1 
        return step


print(Solution().minTaps(35, [1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2])) # 6
print(Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0])) # 1
print(Solution().minTaps(n = 3, ranges = [0,0,0,0])) # -1
print(Solution().minTaps(n = 7, ranges = [1,2,1,0,2,1,0,1])) # 3
print(Solution().minTaps(n = 8, ranges = [4,0,0,0,0,0,0,0,4])) # 2
print(Solution().minTaps(n = 8, ranges = [4,0,0,0,4,0,0,0,4])) # 1
