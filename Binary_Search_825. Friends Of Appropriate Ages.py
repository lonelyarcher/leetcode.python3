""" Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120. """
from typing import List
import bisect
class Solution_BinarySearch: # O(n*logn)
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        for i in range(len(ages)):
            if ages[i] < 14: continue
            left, right = bisect.bisect(ages, ages[i]/2 + 7), bisect.bisect(ages, ages[i])
            if left < i: ans += i - left
            ans += right - i - 1
        return ans

#count sort
from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count, ans, acc = [0] * (max(ages) + 1), 0, []
        for a in ages: count[a] += 1
        for i in range(len(count)):
            if i <= 14: 
                acc.append(0)
                continue
            acc.append(acc[-1] + count[i])
            ans += count[i] * (acc[i] - acc[i//2 + 7] - 1) 
        return ans

print(Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])) #29

print(Solution().numFriendRequests([108,115,5,24,82])) # 3

print(Solution().numFriendRequests([16,16])) #2

print(Solution().numFriendRequests([16,17,18])) #2

print(Solution().numFriendRequests([20,30,100,110,120])) #3