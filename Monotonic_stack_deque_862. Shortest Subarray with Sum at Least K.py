""" Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9 """


'''
First presum is need to calculate subarray sum
when we get a presum at i length s, let's look at the previous presums we have, if there is a sum less or equal to s - K, 
then it is valid subarray for pre to cur, we can update our answer.
There is monotonical feature: if you find more latest/closer pre, the target subarray is shorter.
so we can pop from left of presum array if we find valid, because we no longer need check them at all if valid once, otherwise the i - pre will longer not our choice to find shortest one.
The same time, as greedy as we can, if new presum is less or equal to any right side of array, we can pop too, since it is useless comparing with the new one with less value and closer distance to future presume.
The data structure better for pop from both side is deque
and time complexity will O(n)

'''
from typing import List
import collections
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        st, ans, s = collections.deque([(0, 0)]), float("inf"), 0
        for i in range(1, len(A) + 1):
            s += A[i - 1]
            while st and s < st[-1][0]: st.pop() # greedy to pop right, if we have less presum
            st.append((s, i))
            while s - K >= st[0][0]: ans = min(ans, i - st.popleft()[1]) # if we already find valid index for short length, we don't need check those idx any more, because in future they will be longer than what we had
        return ans if ans < float("inf") else -1

print(Solution().shortestSubarray(A = [1], K = 1)) #1

print(Solution().shortestSubarray(A = [1,2], K = 4)) #-1

print(Solution().shortestSubarray(A = [2,-1,2], K = 3)) #3