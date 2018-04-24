'''
There are n coins in a line. Two players take turns to take one or two coins from
right side until there are no more coins left. The player who take the last coin wins.
Could you please decide the first play will win or lose?
Example n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.
'''

class Solution:
    def coinsInALine(self, n):
        s = {}
        s[1] = True
        s[2] = True
        for i in range(3, n+1):
            '''
            for the first turn
            the first player has the choice to pick one or two, either decision win he will win
            i-1 is the left of coins if he picks one, i-2 is the left of coins if he picks two
            after he picks, the rival will has same strategy to make the decision, that is game theory.
            So if his rival can't win in either case (s[i - 1] or s[i - 2]), he, the first player wins.
            '''
            s[i] = (not s[i-1]) or (not s[i-2])
        return s[n]

for x in range(1, 100):
    print(x, Solution().coinsInALine(x))   