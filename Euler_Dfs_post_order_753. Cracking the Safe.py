""" There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

 

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
 

Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096. """

'''
transfer to graphic p, Hierholzer's algorithm
Euler path vs Euler circuit: each edge is traversed exactly once, circuit will back to start to form a circle
Euler path: exactly two vertices of odd edges
Euler circuit: all even edges
Hierholzer: dfs the Euler circuit, you can only stuck at the original vertex. You can use post-order recording the edges to get a valid path.

'''
import collections
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1: return ''.join(map(str, range(k)))
        start = '0' * (n - 1)
        ans = ''
        seen = set()
        def dfs(start):
            nonlocal ans
            for x in map(str, range(k)):
                ne = start + x
                if ne not in seen:
                    seen.add(ne)
                    dfs(ne[1:])
                    ans += x # post order, once it stuck, we go back to try another edges. this post order will be the answer.
        dfs(start)
        return ans + start

print(Solution().crackSafe(n = 1, k = 2)) # "01", '10'
print(Solution().crackSafe(n = 2, k = 2)) # "00110", "01100", "10011", "11001"
        