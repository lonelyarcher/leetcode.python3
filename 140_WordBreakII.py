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


class DpSolution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mem = {}
        dict = set(wordDict)

        def dfs(i, s, dict):
            if mem.get(i):
                return mem[i]
            mem[i] = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in dict:
                    mem[i] += [s[i:j]] if j == len(s) else [ s[i:j] + " " + x for x in dfs(j, s, dict)]
            return mem[i]

        dfs(0, s, dict)
        return mem[0]

    



s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s2 = DpSolution()
print(s2.wordBreak(s, wordDict))