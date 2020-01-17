""" An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000 """

'''
any two connected nodes, if we choose the parent is the additional node connect to the subTree: sumDist(parent) += numOfNodes(subTree) + sumDist(subTree)
so if we topdown first by post order, we can calculate the each parent by its sub trees.
But we only update the parent with its sub trees, on the contrary, we also need update the child with its parents and other siblings.
so we need to another topdown preorder,  
Error:
1. forget bi-directions, each adjacent list will include its parent, need to exclude parent in the loop
2. in preorder tranversal , forget to recursion to its children
3. when update sub trees, sumDist(subtree) += numOfAllOthers(sums[0] - sums[itself]) + sumDist[parent] - sumDist[itself] - nums[itself]

'''


import collections
from typing import List
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * N
        nums = [1] * N
        g = collections.defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        def post(root, p):
            for nei in g[root]:
                if nei != p: 
                    post(nei, root)
                    nums[root] += nums[nei]
                    ans[root] += nums[nei] + ans[nei]
        def pre(root, p):
            for nei in g[root]:
                if nei != p:
                    ans[nei] += (N - nums[nei]) + (ans[root] - ans[nei] - nums[nei])
                    pre(nei, root)
        post(0, -1)
        pre(0, -1)
        return ans

print(Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]])) #[8,12,6,10,10,10]
            