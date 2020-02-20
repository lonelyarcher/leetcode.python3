""" Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S. """

# Sliding windows, maintain a dict count on each char in t.
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = collections.Counter(t) # target counter
        ans = float('inf'), None, None # help to output result substring from l to r
        j, size, cur = 0, 0, collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] not in ct: continue
            cur[s[i]] += 1
            if cur[s[i]] <= ct[s[i]]:
                size += 1
            while size == len(t):
                if i - j + 1 < ans[0]:
                    ans = i - j + 1, j ,i
                if s[j] in ct: 
                    cur[s[j]] -= 1
                    if cur[s[j]] < ct[s[j]]:
                        size -= 1
                j += 1
        return s[ans[1]:ans[2] + 1] if ans[1] != None else ''

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))  # Output: "BANC"