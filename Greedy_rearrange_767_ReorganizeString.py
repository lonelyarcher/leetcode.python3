""" Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500]. """

"""  
greedy re-order the str group by char, put most frequent char at first, [abcabcaca] => [aaaabbccc]
then insert every other index of empty list. [a, ,a, ,a, ,a, ] => [a, b, a, b, a, c, a, c, a]  step by 2
"""

import math, collections
class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        maxf = max(counter.keys(), key=lambda x: counter[x])
        if counter[maxf] > math.ceil(len(S)/2): return ""
        A = iter([maxf] * counter[maxf] + sum(([k] * v for k, v in counter.items() if k != maxf), []))
        ans = [0] * len(S)
        for i in range(0, len(S), 2):
            ans[i] = next(A) # call next(iterator)
        for i in range(1, len(S), 2):
            ans[i] = next(A)
        return "".join(ans)

    def reorganizeString2(self, S: str) -> str:
        h, counter = math.ceil(len(S)/2), collections.Counter(S)
        maxf = max(counter.keys(), key=lambda x: counter[x])
        A = [maxf] * counter[maxf] + sum(([k] * v for k, v in counter.items() if k != maxf), []) # sum [initial] required if type is not number 
        A[::2], A[1::2] = A[:h], A[h:] # list slice assignment
        return "".join(A) if counter[maxf] <= h else ""

