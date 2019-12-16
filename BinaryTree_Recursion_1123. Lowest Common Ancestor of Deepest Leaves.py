""" Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000. """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Binary Tree problem can be always solved by recursion from root, to its left and right children

Before recursive call: you can set or calculate something like preorder iterate
and you can push sth down to the recursive call

After recursive call, you have the result from the subtree, then you can calculate the result for whole tree, 
Divide & conquer: the problem divided into the root and its left subtree and right subtree. 

the recursive call DFS you can return a count/sum/max/min values, and even a target node like lowest common ancestor.
Something return a pair/tuple is very helpful to solve the problem in one dfs run.

This is question is very good example to use these binary tree top down recursion tricks.
First find what is the key feature of lca of deepest leaves, by draw some examples, like lca([1, 2, 3]) = 1 and lca([1, 2, 3, 4]) = 4
this lca node's two children must have same depth and the depth is max depth.
when top down, you will meet many ld = rd, how can we know which one is deepest, so we can push down the level to leaves to calculate the depth,  
and ask the function to return the node's depth
then if we found equal depth children node, also pass it up by function return. When two equal depth nodes meet, we take the deepest one to pass on and dump the other one.
if two child have same depth, then dump both and pass the current one on.
Don't forget before any recursive call children, check the current node is null or not
"""

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, level):
            if not node: return (level, None)
            l, r = dfs(node.left, level + 1), dfs(node.right, level + 1)
            if l[0] == r[0]: return (l[0], node)
            return (max(l[0], r[0]), l[1] if l[0] > r[0] else r[1])
        return dfs(root, 0)[1]