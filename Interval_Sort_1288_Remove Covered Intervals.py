""" Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
 

Constraints:

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j """
from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        right, covered = float("-inf"), 0
        for i in sorted(intervals, key=lambda i: (i[0], i[1])): # sorted by two keys
            if i[1] <= right: covered += 1
            right = max(right, i[1])
        return len(intervals) - covered

print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]])) #2