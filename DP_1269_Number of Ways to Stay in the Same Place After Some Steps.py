""" You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6 """

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """ 
        state: i for step, j for position of arr
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1] + dp[i - 1][j - 1]
        rolling array can optimize the space to dp[j]
        but in this question arrlen=10^6 >> steps=500, to optimization: the value of dp[0] is only related to 1 if step 1, 2 if step 2, 3 if step 3
        n if step n
        so if arrlen >> step, we only care about the step length of arr
        """
        m = 1000000007
        dp = [1]
        for i in range(1, steps + 1):
            next = []
            for j in range(min(i + 1, arrLen)):
                next.append((0 if j == 0 else dp[j - 1]) + (0 if j >= i else dp[j]) + (0 if j == arrLen - 1 or j >= i - 1 else dp[j + 1]))
            dp = next
        return dp[0] % m
print(Solution().numWays(steps = 3, arrLen = 2)) #4
print(Solution().numWays(steps = 2, arrLen = 4)) #2
print(Solution().numWays(steps = 4, arrLen = 2)) #8
