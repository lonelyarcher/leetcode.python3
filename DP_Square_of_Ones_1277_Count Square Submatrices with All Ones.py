""" Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1 """

""" 
in place calculate, first row and first column keep unchanged, if 1 then it can only be one square of side one.
All other cell inside use DP, dp[i][j] = 1 + min(dp[i - 1][j] above, dp[i][j - 1]left and dp[i - 1][j - 1]leftAbove square #) if m[i][j] == 1 else 0
to save space, all in space, update m[i][j] with dp[i][j], because calculating is one direction, the current cell i, j only depends on calculate cells 
map(sum, m) will return a iterator of sum of each row, sum them again you get the total sum of all the squares of ones
"""
from typing import List
class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                m[i][j] = 0 if m[i][j] == 0 else 1 + min(m[i - 1][j], m[i - 1][j - 1], m[i][j - 1])
        return sum(map(sum, m))


print(Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])) #7