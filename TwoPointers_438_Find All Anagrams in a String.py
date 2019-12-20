""" Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab". """

import collections
from typing import List
class Solution_TwoPointers:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = collections.Counter(p)
        cur = collections.Counter()
        j, ans = 0, []
        for i in range(len(s)):
            cur[s[i]] += 1
            while cur[s[i]] > cnt[s[i]]:
                cur[s[j]] -= 1
                j += 1
            if not cur - cnt and not cnt - cur:  
                # two counter equals ignore the zero count, dict1 == dict2 but zero count will fail, only not cnt1 - cnt2 the negative ones also get ignored
                ans.append(j)
        return ans

class Solution_fixed_length_SlidingWindow: #Since the length of window is fixed to len(p)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = collections.Counter(p)
        cnt_s = collections.Counter()
        ans = []
        for i in range(len(s)):
            cnt_s[s[i]] += 1
            if i >= len(p):
                cnt_s[s[i - len(p)]] -= 1
            if not cnt_s - cnt_p and not cnt_p - cnt_s: 
                ans.append(i - len(p) + 1)
        return ans
s = Solution_fixed_length_SlidingWindow()
print(s.findAnagrams("cbaebabacd", "abc")) #[0, 6]
print(s.findAnagrams("abab", "ab")) #[0, 1, 2]