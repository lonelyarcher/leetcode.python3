""" Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100 """


# follow the row and col, moving the pointer for top to down (row), for right to left(col). 
# if we find first col from right is >= 0, then we know for the next row, grid[row + 1][col] < grid[row][col], 
# so for the next row, we can continue check at this col, no need to back to the right end,
# time complexity: O(m + n)
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, ans = 0, n - 1, 0
        while r < m:
            while c >= 0 and grid[r][c] < 0:
                c -= 1
            ans += n - 1 - c
            r += 1
            if c == -1: 
                break
        ans += (m - r) * n
        return ans

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8