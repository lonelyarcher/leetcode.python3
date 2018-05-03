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

        def transform(w):
            res = inf
            # prepare wordList set
            dict = defaultdict(list)
            for w in wordList:
                for i in range(len(w)):
                    dict[w[:i]+'_'+w[i+1:]].append(w)
            queue = [beginWord]
