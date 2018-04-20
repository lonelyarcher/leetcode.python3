'''
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and - , you and your friend take turns to
flip twoconsecutive "++" into "--" . The game ends when a person can no
longer make a move and therefore the other person will be the winner.
Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++" , return true. The starting player can guarantee a
win by flipping the middle "++" to become "+--+" .
思路：这种博弈类的问题，重点思想就是，你要Minimize你的对手的Profit。在这道
题里面就是有点back tracking的思想，我flip一个如果我的对手不能赢的话，那么我
就赢了。如果我怎么flip我都不能赢对手的话，那我就认输。
'''
class Solution():

    def canWin(self, s):  # not to break down to substring, follow the game, the str flip to next str to the rival. Option to use memorization to cache the result.
        """
        :type s: str
        :rtype: bool
        """
        for k in range(len(s) - 1):
            if s[k:k+2] == '++':
                if not self.canWin(s[:k] + '--' + s[k+2:]): return True
        return False

    def canWin1(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def dp(i, j): # no need to use python string 'contains' ( in, not in ), find (return -1 if not in) and indexof (exception if not in)
            for k in range(i, j):
                if s[k:k+2] == '++':
                    if not dp(i, k - 1) and not dp(k+2, j): return True
            return False
        return dp(0, len(s) - 1)

print(Solution().canWin('++++'))