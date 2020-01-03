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
import collections
''' 
three indices which indice can repeat, like 3 sum problem, don't go DP which solved as unique combination of 3 index
Straightforward, you can just loop three times O(n^3)
like 3 sum, you can optimize by hash first two & result into a count map, res: count, then loop the each res on each A elements a, if a & res == 0
then add the count into the ans
it save the calculation avoid repeated first & values, combine them into a map, still like O(n^3) but avoid a lot of repeating so much faster
'''
class Solution:
    def countTriplets_straightforward(self, A: List[int]) -> int:
        return sum(A[i] & A[j] & A[k] == 0 for i in range(len(A)) for j in range(len(A)) for k in range(len(A)) )
        
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        cnt = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                cnt[A[i]&A[j]] += 1
        return sum(cnt[k] for k in cnt for a in A if a & k == 0)


print(Solution().countTriplets_straightforward([2,1,3])) # 12
print(Solution().countTriplets([2,1,3])) # 12