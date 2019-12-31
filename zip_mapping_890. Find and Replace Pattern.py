""" You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20 """
from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            d, rd = {}, {} # use two map to record w->p and p->w mapping
            for w, p in zip(word, pattern): 
                if w in d and d[w] != p: break
                if p in rd and rd[p] != w: break
                d[w] = p
                rd[p] = w
            else: ans.append(word)
        return ans

    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        return [w for w in words if len(set(w)) == len(set(pattern)) == len(set(zip(w, pattern)))]


print(Solution().findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb")) # Output: ["mee","aqq"]
print(Solution().findAndReplacePattern2(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb")) # Output: ["mee","aqq"]