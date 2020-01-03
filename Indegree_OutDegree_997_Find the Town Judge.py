""" In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N """
from typing import List
import collections
class Solution:
    # O(n^2) check every number for in-degree and out-degree
    def findJudge_straightforward(self, N: int, trust: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for a, b in trust:
            adj[a].add(b)
        for i in range(1, N + 1):
            if not adj[i] and all(i in adj[j] for j in range(1, N + 1) if j != i): return i
        return -1
    # if one person's in-degree is N - 1 and his out-degree is 0, which also in-degree - out-degree == N - 1
    # O(n) just count everyone's in and out degree once
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for a, b in trust:
            count[a] -= 1
            count[b] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1: return i
        return -1

print(Solution().findJudge(N = 2, trust = [[1,2]])) #2
print(Solution().findJudge(N = 3, trust = [[1,3],[2,3]])) #3
print(Solution().findJudge(N = 3, trust = [[1,3],[2,3],[3,1]])) #-1
print(Solution().findJudge(N = 3, trust = [[1,2],[2,3]])) #-1
print(Solution().findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])) #3