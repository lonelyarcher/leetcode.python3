""" Given an array of integers A, find the number of triples of indices (i, j, k) such that:

0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
 

Example 1:

Input: [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
 

Note:

1 <= A.length <= 1000
0 <= A[i] < 2^16 """
from typing import List
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n, ans = 4, 0
        dp = [[0] * n for _ in range(3)]
        for i in range(len(A)):
            dp1 = [row[:] for row in dp]
            for j in range(3):
                dp1[j][A[i]] += 1
            for j in range(0, n):
                dp1[1][A[i] & j] += dp[0][A[i]]
                dp1[2][A[i] & j] += dp[1][A[i]]
            ans += dp1[2][0]
            dp = dp1
        return ans

print(Solution().countTriplets([2,1,3])) # 12