'''
There is a stone game.At the beginning of the game the player picks n piles of
stones in a line.
The goal is to merge the stones in one pile observing the following rules:
At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile. You are to determine the
minimum of the total score.
Example For [4, 1, 1, 4], in the best solution, the total score is 18:
1. Merge second and third piles => [4, 2, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10 Other two examples: [1, 1, 1, 1]
return 8 [4, 4, 5, 9] return 43

dp[i][j]= sum(num[i:j]) + min([dp[i][k]+dp[k+1][j] for k in rang
e(i,j)])。
'''
class Solution():
    def stoneGame(self, a):
        s = {}
        def helper(i, j):
            if i == j:
                return 0
            if (i, j) in s:
                return s[(i, j)]
            s[(i, j)] = sum(a[i:j + 1]) + min([helper(i, k) + helper(k + 1, j) for k in range(i, j)])
            return s[(i, j)]
        return helper(0, len(a)-1)

so = Solution()
print(so.stoneGame([4, 1, 1, 4]))