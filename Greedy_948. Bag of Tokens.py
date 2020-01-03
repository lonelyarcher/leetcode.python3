""" You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.

 

Example 1:

Input: tokens = [100], P = 50
Output: 0
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
 

Note:

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000 """

'''
Greedy, sort the tokens, we always choose to face up the leftest token and face down the rightest token to trade point to power
first faceup as many leftest as you can
then trade the facedown, as long as there are more than two left, and after you trade you can still buy the leftest , you do it, since you can't loose any thing
after on trade, then you do faceup as many as you can
to better coding avoid repeat, define a faceup function to call multiple times
'''

from typing import List
import collections
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        S = 0
        tokens = collections.deque(sorted(tokens))
        def faceup():
            nonlocal S, P
            while tokens and P >= tokens[0]:
                S += 1
                P -= tokens.popleft()
        faceup()
        while len(tokens) > 2 and S and P + tokens[-1] >= tokens[0]:
            S -= 1
            P += tokens.pop()
            faceup()
        return S

print(Solution().bagOfTokensScore([6,0,39,52,45,49,59,68,42,37], 99)) #5