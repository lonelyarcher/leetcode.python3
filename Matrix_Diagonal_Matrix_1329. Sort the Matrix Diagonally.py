""" Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100 """

from typing import List
import collections
# straight forward, loop on all diagonal to get list, sort on it, then overwrite back
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n  = len(mat), len(mat[0])
        mat = [[0] * (m - 1) + row for row in mat]
        for i in range(m + n - 1):
            x, y = 0, i
            arr = []
            while x < m and y < m + n - 1:
                arr.append(mat[x][y])
                x += 1
                y += 1
            arr.sort()
            x, y, j = 0, i, 0
            while x < m and y < m + n - 1:
                mat[x][y] = arr[j]
                j += 1
                x += 1
                y += 1
        return [row[m - 1:] for row in mat]
# Better solution, observe ont the same diagonal line, the difference between row# and col# are all same and distinct from other diagonal lines
# so we globally collect all the diagonal lists, and sort, then put them back follow the natural row/col increasing order
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n  = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        for a in d.values():
            a.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        return mat

print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])) # Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]