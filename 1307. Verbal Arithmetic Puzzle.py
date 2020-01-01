""" Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result). 
Return True if the equation is solvable otherwise return False.

Constraints:

2 <= words.length <= 5
1 <= words[i].length, results.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10.
"""

from typing import List
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        d = {}
        e = result + "-" + " ".join(words)
        def dfs(i, cur, res):
            if i == len(e):
                return res == cur
            if res < 0: return False
            if e[i].isalpha():
                if e[i] in d:
                    return dfs(i + 1, cur * 10 + d[e[i]], res)
                else:
                    for j in range(10):
                        if j not in d.values() and (cur > 0 or j > 0):
                            d[e[i]] = j
                            if dfs(i + 1, cur * 10 + j, res): 
                                return True
                            d.pop(e[i])
                    return False
            else:
                return dfs(i + 1, 0, cur if e[i] == "-" else res - cur)
        return dfs(0, 0, 0)

s = Solution()
print(s.isSolvable(words = ["AB","A"], result = "CD")) # t 1 + 1 = 2
print(s.isSolvable(words = ["SEND","MORE"], result = "MONEY")) # t 9567 + 1085 = 10652
print(s.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")) # t 650 + 68782 + 68782 = 138214
print(s.isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY")) # t
print(s.isSolvable(words = ["LEET","CODE"], result = "POINT")) # f