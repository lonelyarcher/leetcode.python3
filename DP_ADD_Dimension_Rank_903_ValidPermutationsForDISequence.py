""" We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

 

Example 1:

Input: "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
 

Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}. """

"""
First dfs to find all the permutation is a option, but the time complexity is O(n!) but n = S.length up to 200, so N! will be TLE (time limit exceeds)

n = len(S) + 1
Permutation from 0 to (n - 1) based on S decreasing or increasing, the number itself doesn't matter, [1, 2, 3] will have same permution number as [2, 5, 7] for whatever DI sequences
The relative rank between the numbers matters.
This problem can be solved high possibly by DP, the hardest part is define the state, the first i numbers is one of state for sure, but it is not enough
You can't decide when new D/I character appear, the new coming number depends on the last number
You can't fix the last number, because that is same as DFS = O(N!) time complexity. 
Because the rank matters, so let's define the second element of state as the rank of the last number in all left numbers, 
like if you have last as 1]  2,3 left, will be same as 4] 5, 6, important the rank is before you choose

which rank of last number is smallest in left numbers
Let's take a example DID [0, 1, 2, 3]
first choose  0, dp[1][0] = 1, choose 1 dp[1][1] = 1, choose 2 dp[1][2] = 1, choose 3 dp[1][3] = 1
then if D, so the next number need be small than the last one
dp[2][0] = dp[1][1] + dp[1][2] + dp[1][3]  if previous rank is GT 0, which mean the last number is GT the current choose
else if I： dp[2][2] = dp[1][0] + dp[1][1] + dp[1][2]

so we can deduct: dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1,  n - i + 2) if D  //why n - i + 1, total n, i - 1 used before you choose, then n - (i - 1) + 1 is closed range
same for I: dp[i][j] = sum(dp[i - 1][k] for k in range(0, j + 1) //why j + 1, before you choose
And the final answer will be: dp[n][0]
time O(n^2) space O(n)
"""
import itertools
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S) + 1
        dp = [[0] * n for i in range(n + 1)]
        dp[1] = [1] * n
        for i in range(2, n + 1):
            for j in range(0, n):
                if S[i - 2] == 'D':
                    dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1,  n - i + 2))
                else:
                    dp[i][j] = sum(dp[i - 1][k] for k in range(0, j + 1))
        return dp[n][0] % 1000000007



# Optimization, rolling array to reduce the space, and sum of continuous number can be reduced to O(1) if pre-calculate the pre-sum = accumulate sum
# time O(n), space O(n) 
    def numPermsDISequence_2(self, S: str) -> int:
        n = len(S) + 1
        dp = list(itertools.accumulate([1] * n, initial=0))
        for i in range(2, n + 1):
            ndp = [0] * n
            for j in range(0, n):
                if S[i - 2] == 'D':
                    ndp[j] = dp[n - i + 2] - dp[j + 1]
                else:
                    ndp[j] = dp[j + 1] - dp[0]
            dp = list(itertools.accumulate(ndp, initial=0))
        return dp[1] % 1000000007

print(Solution().numPermsDISequence("DID"))  # 5
print(Solution().numPermsDISequence_2("DID"))  # 5