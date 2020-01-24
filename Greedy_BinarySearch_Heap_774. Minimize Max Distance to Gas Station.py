""" On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct. """

'''
Greedy, insert the new station into the gaps between original stations, you always find the gap with greater distances. so we can greedy solve it with max-heap
max-heap pop the current largest dist, if there are already i stations in this gap, then after add new one, will be i + 1, new distance: d * i / (i + 1)
the time complexity is O(K*log(N))
This question K >> N, so we can optimize to first add multiple new station to max_dist = (end - start) / K
'''

from typing import List
import heapq, math
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        N = len(stations)
        heap = [(stations[i] - stations[i + 1], 1) for i in range(N - 1)]
        max_d = (stations[N - 1] - stations[0]) / (K + 1)
        heapq.heapify(heap)
        while K:
            d, s = heapq.heappop(heap)
            ns = s + 1 if -d <= max_d else math.ceil(-d / max_d) 
            nd = d * s / ns
            K -= ns - s
            heapq.heappush(heap, (nd, ns))
        return -heap[0][0]

'''
find possible max_dist, check if this distance we can make it with K station
'''

    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        N = len(stations)
        def check(dist):
            n = 0
            for i in range(N - 1):
                n += (stations[i + 1] - stations[i]) // dist
                if n > K: return False
            return True
        l, r = 0, (stations[N - 1] - stations[0]) / K
        while l < r - 0.00001:
            mid = (l + r) / 2
            if check(mid):
                r = mid
            else:
                l = mid
        return l
print(Solution().minmaxGasDist([10,19,25,27,56,63,70,87,96,97], 3)) # 9.66667
print(Solution().minmaxGasDist(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9)) # 0.5