""" A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000. """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Level order by a queue, we use queue we can find the first uncompleted node is on the queue head q[0]
once add both children to it, we pop out head, then move the next.
Two trick point:
1. initiate with another complete tree, so need to do level traversal to first uncompleted one
2. once you find a uncompleted node, before you break the while loop, add its left child into the queue if it has
'''


import collections
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque()
        self.q.append(root)
        while self.q:
            if not self.q[0].left:
                break
            if not self.q[0].right: 
                self.q.append(self.q[0].left)
                break
            node = self.q.popleft()
            self.q.append(node.left)
            self.q.append(node.right)
        
    def insert(self, v: int) -> int:
        node = TreeNode(v)
        p = self.q[0]
        if not p.left:
            p.left = node
        else:
            p.right = node
            self.q.popleft()
        self.q.append(node)
        return p.val
        

    def get_root(self) -> TreeNode:
        return self.root
