""" Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9 """
from typing import List
class Solution:
    """ normal solution, use a new list to collect intervals """
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        l, r = toBeRemoved
        ans = []
        for i in intervals: 
            if i[1] < l or i[0] > r: ans.append(i) # if no intersected
            else:
                if i[1] > l and i[0] < l: ans.append([i[0], l]) # if intersect with l
                if i[0] < r and i[1] > r: ans.append([r, i[1]]) # if intersect with r
        return ans
    """ reverse the range, then you can delete elements while iteration, use list pop and insert """
    def removeInterval2(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        for i in reversed(range(len(intervals))): 
            if intervals[i][0] < toBeRemoved[1] and intervals[i][1] > toBeRemoved[0]: # if interval intersected 
                x, y = intervals.pop(i)
                intervals.insert(i, [toBeRemoved[1], y])
                intervals.insert(i, [x, toBeRemoved[0]])
        return filter(lambda x: x[0] < x[1], intervals)
    """ double loop in comprehesion [x for a in b for x in a], first outer loop then inner loop """
    def removeInterval3(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        return [[x, y] for a, b in intervals for x, y in ((a, min(b, toBeRemoved[0])), (max(a, toBeRemoved[1]), b)) if x < y]