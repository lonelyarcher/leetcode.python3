""" We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8 """



'''

merge interval is easy after sorting, in this case we can avoid sorting on all intervals in all schedules. To utilize each schedules are pre-sorted. 
n = len(schedules)
We can reduce to log(n) by a min-heap to add each head of schedules
Also we can solve the problem by sweepline from left to right, of course need sort first.
'''
from heapq import *

class Solution:
    def employeeFreeTime(self, schedule):
        #sort by heap
        s = [a[::-1] for a in schedule]
        A, heap, ans = [], [], []
        for i, a in enumerate(s):
            heappush(heap, (a.pop(), i))
        while heap:
            interval, i = heappop(heap) # should pop by heappop;  tuple is not mutable
            A.append(interval)
            if s[i]:
                heappush(heap, (s[i].pop(), i))
        # merge from left to right
        pre = A[0]
        for cur in A[1:]:
            if cur[0] > pre[1]:
                ans.append([pre[1], cur[0]])
                pre = cur
            else:
                pre[1] = max(pre[1], cur[1])
        return ans

    # sweepline, convert interval to event
    def employeeFreeTime(self, schedule):
        events = []
        for s in schedule:
            for i in s:
                events.append((i[0], -1)) # start usually +1, but 
                events.append((i[1], 1))
        events.sort()
        pre, count, ans = None, 0, []
        for e in events:
            if pre != None and count == 0:
                ans.append([pre, e[0]])
            pre = e[0]
            count += e[1]
        return ans

print(Solution().employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])) # [[3, 4]]
print(Solution().employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])) # [[5,6],[7,9]]


