""" Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1
 

Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters. """

import functools
class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def f(l, r):
            if l >= r: return 0
            if s[l] == s[r]:
                return f(l + 1, r - 1)
            else:
                return 1 + min(f(l + 1, r), f(l, r - 1))
        return f(0, len(s) - 1)