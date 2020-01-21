""" Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase. """

from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        ans = [float('inf')] * n
        pre = -1
        for i in range(n):
            if S[i] == C:
                ans[i] = 0
                pre = i
            elif pre >= 0:
                ans[i] = i - pre
        pre = -1
        for i in range(n)[::-1]:
            if S[i] == C:
                pre = i
            elif pre >= 0:
                ans[i] = min(ans[i], pre - i)
        return ans

print(Solution().shortestToChar("aaba", "b")) #Output: [2,1,0,1]
print(Solution().shortestToChar(S = "loveleetcode", C = 'e')) #Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]