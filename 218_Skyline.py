import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, n = 0, len(buildings)
        heap = []
        while heap or i < n:
            if not heap or (i < n and buildings[i][0] <= -heap[0][1]):
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(heap, [-buildings[i][2], -buildings[i][1]])
                    i += 1
            else:
                x = -heap[0][1]
                while heap and -heap[0][1] <= x:
                    heapq.heappop(heap)
            height = 0 if not heap else -heap[0][0]
            if not res or res[-1][1] != height:
                res.append([x, height])
        return res

s = Solution()
print(s.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20
, 10], [19, 24, 8] ]))
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].