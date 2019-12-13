""" In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters. """
from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            for a, b in zip(words[i - 1], words[i]):
                if order_map[a] > order_map[b]: return False
                elif order_map[a] < order_map[b]:  break
            else:
                if len(words[i - 1]) > len(words[i]): return False
        return True
print(Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")) #True
print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")) #False
print(Solution().isAlienSorted(["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")) #False
