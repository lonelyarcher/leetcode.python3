""" A tree rooted at node 0 is given as follows:

The number of nodes is nodes;
The value of the i-th node is value[i];
The parent of the i-th node is parent[i].
Remove every subtree whose sum of values of nodes is zero.

After doing so, return the number of nodes remaining in the tree.

 

Example 1:



Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
 

Constraints:

1 <= nodes <= 10^4
-10^5 <= value[i] <= 10^5
parent.length == nodes
parent[0] == -1 which indicates that 0 is the root. """

from typing import List
import collections
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        adj = collections.defaultdict(list)
        for i, p in enumerate(parent):
            adj[p].append(i)
        def dfs(root):
            sub_sum, sub_num = value[root], 1
            for nei in adj[root]:
                a, b = dfs(nei)
                sub_sum += a
                sub_num += b
            if sub_sum == 0:
                sub_num = 0
            return sub_sum, sub_num
        return dfs(-1)[1] - 1 # minus one because there is a fake node -1 point to 0
print(Solution().deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1])) # output: 2
