import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord == endWord: return [[endWord]]
        # prepare wordlist dict
        dict = collections.defaultdict(list)
        for w in wordlist + [endWord]:
            for i in range(len(w)):
                dict[w[:i]+'_'+w[i+1:]].append(w)
        res = []
        queue = [[beginWord]]
        while queue:
            path = queue.pop(0)
            if res and len(res[0]) <= len(path): return res # while loop stop condition: once find the endWord and finish this step of path.
            for i in range(len(path[-1])):
                k = path[-1][:i]+'_'+path[-1][i+1:]
                if k in dict:
                    for nex in dict[k]:
                        if nex == endWord:
                            res.append(path + [endWord])
                        elif nex not in path: 
                            queue.append(path+[nex])
        return res

# test
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
so = Solution()
ans = so.findLadders(beginWord, endWord, wordList)
print(ans)