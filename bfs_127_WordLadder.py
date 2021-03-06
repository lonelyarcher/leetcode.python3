'''
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its
length 5.
https://leetcode.com/problems/word-ladder-ii/
思路： 就是一个BFS。然后存一个visited免得重走。
'''

from math import inf
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord: return 0
        cnt = 1
        visited = set() # not necessary if we can remove the visited word from dict
        # prepare wordList set
        dict = defaultdict(list)
        wordList.add(endWord)
        for w in wordList:
            for i in range(len(w)):
                dict[w[:i]+'_'+w[i+1:]].append(w)
        queue = [beginWord]
        while queue:
            n = len(queue)
            visited.update(queue)
            for i in range(n):
                w = queue.pop(0)
                for j in range(len(w)):
                    tmp = w[:j]+'_'+w[j+1:]
                    if tmp in dict:
                        for nex in dict[tmp]:
                            if nex == endWord: return cnt + 1
                            if nex not in visited:
                                queue.append(nex)
            cnt += 1
        return -1

wordList = {"hot","dot","dog","lot","log"}
beginWord = "hit"
endWord = "cog"
so = Solution()
a = so.ladderLength(beginWord, endWord, wordList)
print(a)

