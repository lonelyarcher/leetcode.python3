""" Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
Example 4:

Input: events = [[1,100000]]
Output: 1
Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5 """

'''
Greedy, discretely go through the index from 1 to 100000, add the events into a heap by ending time'
pop out the smallest ending time if heap has events, increase the count for answer
You need clear all the event end at this index.
'''

from typing import List
import heapq, collections
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0
        s = collections.defaultdict(list)
        for e in events:
            s[e[0]].append(e)
        heap = []
        for i in range(100001):
            for ei in s[i]:
                heapq.heappush(heap, ei[1])
            if heap:
                cur = heapq.heappop(heap)
                ans += 1
            while heap and heap[0] == i: # clear all the events end at i
                heapq.heappop(heap)
        return ans

        




print(Solution().maxEvents([[1,2],[2,3],[3,4]])) #3
print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]])) #4
print(Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])) #4
print(Solution().maxEvents([[1,100000]])) #1
print(Solution().maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])) #7
