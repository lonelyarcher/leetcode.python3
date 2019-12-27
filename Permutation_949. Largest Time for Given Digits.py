""" Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9 """

import itertools
from typing import List
class Solution:
    def largestTimeFromDigits_itertools(self, A: List[int]) -> str:
        return max((f'{a[0]}{a[1]}:{a[2]}{a[3]}' for a in itertools.permutations(A) if a[:2] < (2, 4) and a[2] < 6), default="")

    def largestTimeFromDigits(self, A: List[int]) -> str:
        p, seen = [], set()
        def permute(s):
            if len(s) == 4:
                p.append(s)
            else:
                for j in range(len(A)):
                    if j not in seen:
                        seen.add(j)
                        permute(s + str(A[j]))
                        seen.remove(j)
                        
        permute("")
        return max((a[:2] + ':' + a[2:] for a in p if int(a[:2]) < 24 and int(a[2]) < 6), default=None)
print(Solution().largestTimeFromDigits([1,2,3,4])) # "23:41"
print(Solution().largestTimeFromDigits([0,0,0,0])) # "00:00"
print(Solution().largestTimeFromDigits([5,5,5,5])) # None