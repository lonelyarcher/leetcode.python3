""" We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000 """

#Quick Select O(n) time complexity
''' partition: 
    1. set pivot = arr[r]
    2. set smaller front i = l
    3. loop point j in range(l, r) l to r - 1
    4. if arr[j] < pivot, swap(i, j) and i += 1
    5. end loop, swap r and i
    6. return i, all arr[0:i + 1] including i <= pivot
'''
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(idx):
            return points[idx][0] * points[idx][0] + points[idx][1] * points[idx][1]
        def swap(i, j):
            points[i], points[j] = points[j], points[i]
        def partition(l, r):
            i = l
            for j in range(l, r):
                if dist(j) < dist(r):
                    swap(i, j)
                    i += 1
            swap(i, r)
            return i
        l, r = 0, len(points) - 1
        while l <= r:
            p = partition(l, r)
            if p == K - 1: return points[:K]
            if p < K - 1: l = p + 1
            else: r = p - 1

print(Solution().kClosest(points = [[1,3],[-2,2]], K = 1)) #[[-2,2]]
print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)) #[[3,3],[-2,4]] or [[-2,4],[3,3]]
        
