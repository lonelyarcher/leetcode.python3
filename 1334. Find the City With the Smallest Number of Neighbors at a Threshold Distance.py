""" There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:



Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:



Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct. """


# Bellman_Ford algorithm, O(V*E)
# O(N*N*E) = O(N^4)
# 0. dist[] to inf, except dist[start] = 0
# 1. loop n - 1 times
# 2. loop each edges (no need adj list), update dist[e] = min(dist[e], dist[s] + w)

from typing import List
import collections
from heapq import *

class Solution_Bellman_Ford:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans = []
        for i in range(n):
            dist = [float('inf')] * n
            dist[i] = 0
            for _ in range(n):
                for s, e, w in edges:
                    dist[e] = min(dist[e], dist[s] + w)
                    dist[s] = min(dist[s], dist[e] + w)
            ans.append((sum(d <= distanceThreshold for d in dist), -i))
        return -min(ans)[1]

# heap, dist, settled, adj, time O(E + V*log(V)), total V(E + V*logV)
# 0. while len(settled) < n and heap
# 1. add (dist[v], v) into heap, 
# 2. pop min dist, s, 
# 3. if in settled continue
# 4. add into settle, 
# 5. loop s' neighbors, 
# 6. update dist[e], 
# 7. add (dist[e], e) into heap (e can be pushed into heap multiple times)
class Solution_Dijkstra:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = collections.defaultdict(list)
        for s, e, w in edges:
            adj[s].append([w, e])
            adj[e].append([w, s])
        minNei, ans = float('inf'), -1
        for i in range(n):
            dist = [float('inf')] * n
            dist[i] = 0
            settled = set()
            heap = [[0, i]]
            while len(settled) < n and heap:
                _, s = heappop(heap)
                if s in settled: continue
                settled.add(s)
                for w, e in adj[s]:
                    dist[e] = min(dist[e], dist[s] + w)
                    heappush(heap, [dist[e], e])
            count = sum(1 for d in dist if d <= distanceThreshold)
            if count <= minNei: 
                minNei = count
                ans = i
        return ans

# Floyd O(V ^ 3)
# 1. set dist = inf for all pairs
# 2. dist[i][i] = 0, dist[s][e] = w for s, e, w in edges (no need for adj list)
# 3. tri-loop by k, by i, by j, dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

class Solution_Floyd:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        for i in range(n): dist[i][i] = 0
        for s, e, w in edges: 
            dist[s][e] = w
            dist[e][s] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
        return -min((sum(d <= distanceThreshold for d in dist[i]), -i) for i in range(n))[1]


s1, s2, s3 = Solution_Bellman_Ford(), Solution_Dijkstra(), Solution_Floyd()
print(s1.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)) # 3
print(s1.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)) # 0
print(s2.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)) # 3
print(s2.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)) # 0
print(s3.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)) # 3
print(s3.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)) # 0

