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

use segment tree can optimize to O(n*log(n)), when count , add/sub(x1, x2) into the count
"""

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        pass

print(Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])) #6
print(Solution().rectangleArea([[0,0,1000000000,1000000000]])) #49