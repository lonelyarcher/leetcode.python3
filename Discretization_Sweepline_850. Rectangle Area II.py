""" We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectangles[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer. """


"""
Sweepline to calculate the area between y and pre_y
for each y, use Discretization to avoid the merge n intervals O(n^2) time, by count all the 2 * n point, then sum the x2 - x1 if count else 0 to get covered x axis

Sweeping line:
each interval represent as: [y, x1, x2, type (1 for income, 0 for leave)]
sorted by y, then begin to scan

discretization need maintain: 
x: sorted x value set: for all possible x value from left to right.
xi: map from x value to its index for discret
count for index 0 to len(x) - 2, number of overlaps between i and i + 1 

scan n y values, each y count n x values, so total is O(n^2)

use segment tree/BIT can optimize to O(n*log(n)), when count , add/sub(x1, x2) into the count
"""
from typing import List
import itertools
class Solution:

    class BIT:
        def __init__(self, n):
            self.bit = [0] * (n + 1)
        def update(self, i, val):
            i += 1
            while i < len(self.bit):
                self.bit[i] += val
                i += i & -i
        def query(self, i):
            ans = 0
            i += 1
            while i > 0:
                ans += self.bit[i]
                i -= i & (-i)
            return ans

    class Node(object):
        def __init__(self, start, end):
            self.start, self.end = start, end
            self.total = self.count = 0
            self._left = self._right = None

        @property
        def mid(self):
            return (self.start + self.end) // 2

        @property
        def left(self):
            self._left = self._left or type(self)(self.start, self.mid)
            return self._left

        @property
        def right(self):
            self._right = self._right or type(self)(self.mid, self.end)
            return self._right

        def update(self, i, j, val):
            if i >= j: return 0
            if self.start == i and self.end == j:
                self.count += val
            else:
                self.left.update(i, min(self.mid, j), val)
                self.right.update(max(self.mid, i), j, val)

            if self.count > 0:
                self.total = X[self.end] - X[self.start]
            else:
                self.total = self.left.total + self.right.total

            return self.total
        

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        x = sorted(set(itertools.chain(*[[r[0], r[2]] for r in rectangles])))
        xi = {v: i for i, v in enumerate(x)}
        count = [0] * (len(x) - 1)
        l = []
        for x1, y1, x2, y2 in rectangles:
            l.append((y1, x1, x2, 1))
            l.append((y2, x1, x2, -1))
        l.sort()
        pre_y, sum_x, area = l[0][0], 0, 0
        for y, x1, x2, d in l:
            area += (y - pre_y) * sum_x
            pre_y = y
            for i in range(xi[x1], xi[x2]):
                count[i] += d
            sum_x = sum((nex_x - cur_x if c else 0) for cur_x, nex_x, c in zip(x, x[1:], count))
        return area % 1000000007


print(Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])) #6
print(Solution().rectangleArea([[0,0,1000000000,1000000000]])) #49

