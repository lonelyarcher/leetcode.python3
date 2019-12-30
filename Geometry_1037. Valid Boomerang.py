""" A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100 """

import math
from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dist = lambda p1, p2: math.sqrt((p1[0] - p2[0]) **2 + (p1[1] - p2[1])**2)
        a, b, c = points
        d = [dist(a, b), dist(a, c), dist(b, c)]
        d.sort()
        return abs(d[0] + d[1] - d[2]) > 0

    def isBoomerang2(self, points: List[List[int]]) -> bool:
        a, b, c = points
        return (a[0] - b[0]) * (a[1] - c[1]) != (a[1] - b[1]) * (a[0] - c[0])

print(Solution().isBoomerang([[1,1],[2,3],[3,2]]))  # t
print(Solution().isBoomerang([[1,1],[2,2],[3,3]]))  # f
print(Solution().isBoomerang2([[1,1],[2,3],[3,2]]))  # t
print(Solution().isBoomerang2([[1,1],[2,2],[3,3]]))  # f