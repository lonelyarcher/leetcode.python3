""" There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 

Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously. """

'''
Assume you have a max courses list, sort it by ending time.
at each ending time, the sum of courses begin before it can not exceed the ending time.
If exceed, then it means it has overlaping, you need remove one, we can greedy remove the longest one.
why remove longest one, because it must remove, so it is most helpful to solve the problem

'''

from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        que=[]
        cur=0
        for t,d in courses:
            heapq.heappush(que,-t)
            cur+=t
            if cur>d:
                cur+=heapq.heappop(que)
        return len(que)

print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])) # 3 