""" Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
 

Constraints:

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5 """

"""
Problem like find max/min square/rectangle in matrix of 0/1 or any number, there is always dp solution: s((x0, y0), (x1, y1)) = dp[x1][y1] - dp[x0][y1] - dp[x1][y0] + dp[x0][y0]
dp[x][y] can always pre-calculate in presum two dimension array from 0 to len(mat)
then to find max side length, since valid length is monotonical, if x1 is valid, all the x < x1 should be valid
1. we can use binary search to find answer, by m*n*log(n)
2. we can monotonical increasing search for length in loop, time complexity will be m*n
"""

from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for i in range(m + 1)] 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] + mat[i - 1][j - 1] - presum[i - 1][j - 1]
        def check(l):
            for i in range(l, m + 1):
                for j in range(l, n + 1):
                    s = presum[i][j] - presum[i - l][j] - presum[i][j - l] + presum[i - l][j - l]
                    if s <= threshold: return True
            return False
        l, r = 0, 1 + min(m, n)
        while l < r:
            mid = (l + r)//2
            if not check(mid):
                r = mid
            else: l = mid + 1
        return l - 1

class Solution2:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        presum = [[0] * (n + 1) for i in range(m + 1)] 
        s = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] + mat[i - 1][j - 1] - presum[i - 1][j - 1]
                if s <= i and s <= j and presum[i][j] - presum[i - s][j] - presum[i][j - s] + presum[i - s][j - s] <= threshold: s += 1
        return s
       

s = Solution2();
print(s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4)) #2
print(s.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1)) #0
print(s.maxSideLength(mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6)) #3
print(s.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184)) #2