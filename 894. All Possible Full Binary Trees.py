""" A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20 """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        ans = []
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        for i in range(1, N - 1, 2):
            for l in self.allPossibleFBT(i): 
                for r in self.allPossibleFBT(N - 1 - i):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans

print(len(Solution().allPossibleFBT(7)))