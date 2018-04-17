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