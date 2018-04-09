class DfsSolution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        dict = set(wordDict)
        res = []
        self.dfs(res, [], s, dict)
        return res

    def dfs(self, res, path, s, dict):
        if not s:
            res.append(" ".join(path))
            return 
        for i in range(1, len(s) + 1):
            if s[:i] in dict:
                self.dfs(res, path + [s[:i]], s[i:], dict)

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