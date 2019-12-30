""" Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result). 
Return True if the equation is solvable otherwise return False.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true
Example 4:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, results.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10. """







"""
First is DFS problem, it will take O(10!) * 5 * 7, TLE, if not pruning well
1. native solution: assign characters along the words and results, if sum(words) == results, then succeed, the problem is backtrack too later only at the final step.
2. better solution is vertical calculation on each digit from smallest/right to largest/left or by columns
like  
  SEND
+ MORE
------
 MONEY
 first columnL DEY, then NRE, EON SMO, __M, each column we pruning the invalid branches. It will get much faster. ~ 1000ms

When we do the DFS, key part is to assign a dictionary for { char: digit[0-9] }, by back track, we use only one dict, try unused 0 to 9, and if leading character can't be 0
Recursively, if one of assignment succeed, we return true. after recursive call one dfs, we reset the dict assignment to None. After try all possibilities, none succeeds, then we return False

for column we recursive call each assignment
after all assigned in this column i, we calculate the result[i] - word[0][i] - ..- word[n][i], buy reduce function tools on operator.sub
if the reduce result equals to zero, we return as recursive dfs call on i + 1 column until reach len(result), all columns cleared then return True at the final recursion, result is of course longer than any of word


 for easy implementation: 
    1. we reverse the words and result, then we can natural i begin with 0
    2. put all leading character into a set, easy to exclude the invalid assignment zero to them
    3. put carry in dfs carry arguments, because we may have carry to higher digits
"""

from typing import List
import operator
from functools import reduce
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        d = {k: None for s in words + [result] for k in s }
        leading = {w[0] for w in words} | {result[0]}
        rev = [result[::-1]] + [w[::-1] for w in words]
        def dfs(i, carry) -> bool: 
            if i == len(result): return carry == 0
            col = [r[i] for r in rev if i < len(r)]
            used = set(d.values())
            for c in set(col):
                if d[c] == None:
                    for v in (i for i in range(c in leading, 10) if i not in used):
                        d[c] = v
                        if dfs(i, carry): return True # recursion on the same column i, for next assignment
                        d[c] = None # backtrack on each column like here
                    return False
            res = reduce(operator.sub, (d[c] for c in col)) + carry
            if res % 10 == 0: return dfs(i + 1, res//10) # move the recursion to next column i + 1
            else: return False
        return dfs(0, 0)

print(Solution().isSolvable(words = ["A","B"], result = "A")) # True
print(Solution().isSolvable(words = ["SEND","MORE"], result = "MONEY")) # True
print(Solution().isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")) # True
print(Solution().isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY")) # True
print(Solution().isSolvable(words = ["LEET","CODE"], result = "POINT")) #  False