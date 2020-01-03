""" Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

 

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
 

Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000 """
import collections
from typing import List
class Solution:
    def canReorderDoubled_1(self, A: List[int]) -> bool:
        A.sort(key=abs)
        map = collections.defaultdict(int)
        for a in A:
            p = a / 2 
            if map[p] > 0:
                map[p] -= 1
            else:
                map[a] += 1
        return not sum(map.values())

# better solution, sort in count, a little fast, and sort by abs
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        K = sorted(cnt.keys(), key=abs)
        for k in K:
            if cnt[k] > cnt[2 * k]:
                return False
            else:
                cnt[2 * k] -= cnt[k]
        return True

print(Solution().canReorderDoubled_1([0,0,0,0,0,0])) #True
print(Solution().canReorderDoubled_1([4,-2,2,-4])) #True
print(Solution().canReorderDoubled_1([1,2,4,16,8,4])) #False

print(Solution().canReorderDoubled([0,0,0,0,0,0])) #True
print(Solution().canReorderDoubled([4,-2,2,-4])) #True
print(Solution().canReorderDoubled([1,2,4,16,8,4])) #False