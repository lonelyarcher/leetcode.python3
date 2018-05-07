'''
291 Word Pattern II
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in
pattern and a non-empty substring in str.
Examples: pattern = "abab", str = "redblueredblue" should return true. pattern =
"aaaa", str = "asdasdasdasd" should return true. pattern = "aabb", str =
"xyzabcxzyabc" should return false. Notes: You may assume both pattern and str
contains only lowercase letters.
https://leetcode.com/problems/word-pattern-ii/
'''

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def dfs(p, s, dic):
            if not p and not s: return True
            if not p or not s: return False
            if p[0] in dic:
                if dic[p[0]] != s[:len(dic[p[0]])]: return False
                return dfs(p[1:], s[len(dic[p[0]]):], dic)
            for i in range(1, len(s)):
                dic[p[0]] = s[:i]
                dfs(p[1:], s[i:], dic)
        return dfs(pattern, str, {})
# test