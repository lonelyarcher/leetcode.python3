""" For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]
 

Note:

1 <= N <= 1000 """

'''
N <= 1000, it should be DP or recursion by divide & conquer, how to sub or divide list of N is problem.
if you cut half by half, 1 - N, => 1 - N//2, N//2, N, you will meet the merge problem, basically you need check all again so it didn't help for solve.
Let's look at the condition no k, A[k] * 2 = A[i] + A[j], left side must be a even number, right sides A[i] and A[j] must be both even or odd
so if we have first half odd, second half even numbers, which no k can found satisfy i, j between two parts, then we don't have merge problem
if first odd part is beautiful array and the second even part is beautiful array, the whole N is too.
from n beautiful array, we can build 2*n, by put all odd first, then even after. odd: [2 * i - 1 for i in n] even: [2 * i for i in n]

'''
import math
from typing import List
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1: return [1]
        return [2 * i - 1 for i in self.beautifulArray(math.ceil(N/2))] + [2 * i for i in self.beautifulArray(N//2)]

# sort by reversed binary string reversally, so odd will in front of even, then in odd number we left shift on bit are compare sub N/2 array 
class Solution2:
    def beautifulArray(self, N: int) -> List[int]:
        return sorted(range(1, N + 1), reverse=True, key=lambda x: bin(x)[:1:-1] ) # why 1, because we need get rid of "0b" in front of binary represent string, otherwise b > 1 or 0

s = Solution()
for i in range(1, 7):
    print(s.beautifulArray(i))

s = Solution2()
for i in range(1, 7):
    print(s.beautifulArray(i))