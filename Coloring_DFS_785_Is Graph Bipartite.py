""" Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j]. """
from typing import List
# use set to dfs, set A.update(B) = A|B, A.intersection(B) = A & B, A - B difference, A ^ B symmetric difference, ^1 to toggle between 0 and 1 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = [set(), set()]
        seen = set()
        def dfs(v, i):
            seen.add(v)
            A[i].add(v)
            A[i ^ 1].update(graph[v])
            for j in graph[v]:
                if j not in seen: dfs(j, i ^ 1)
        for v in range(len(graph)):
            if v not in seen: dfs(v, 0)
        return len(A[0]) + len(A[1]) == len(graph)

class Solution_coloring:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        def dfs(v, i):
            color[v] = i
            for j in graph[v]:
                if color[j] and color[j] != 3 - i: return False
                if not color[j] and not dfs(j, 3 - i): return False
            return True
        for v in range(len(graph)):
            if not color[v] and not dfs(v, 1): return False
        return True

print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]])) #True
print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])) #False


print(Solution_coloring().isBipartite([[1,3], [0,2], [1,3], [0,2]])) #True
print(Solution_coloring().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])) #False
        