'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

class DfsSolution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        dict = set(wordDict)
        return self.dfs(0, s, dict)


    def dfs(self, i, s, dict):
        res = []
        for j in range(i, len(s) + 1):
            if s[i:j] in dict:
                res += [s[i:j]] if j == len(s) else [s[i:j] + " " + x for x in self.dfs(j, s, dict)]
        return res

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s1 = DfsSolution()
print(s1.wordBreak(s, wordDict))

import collections
class DpSolution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mem = collections.defaultdict(list)
        dict = set(wordDict)

        def dfs(i, s, dict):
            if mem.get(i):
                return mem[i]
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in dict:
                    mem[i] += [s[i:j]] if j == len(s) else [ s[i:j] + " " + x for x in dfs(j, s, dict)]
            return mem[i]

        dfs(0, s, dict)
        return mem[0]


    def wordBreak2(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                        for j in range(i+1, len(s)+1)
                        if s[i:j] in wordDict
                        for tail in sentences(j)]
            return memo[i]
        return sentences(0)
    



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s2 = DpSolution()
print(s2.wordBreak(s, wordDict))