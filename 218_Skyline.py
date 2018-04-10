import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heapq.heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline

print s.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20
, 10], [19, 24, 8] ])
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].