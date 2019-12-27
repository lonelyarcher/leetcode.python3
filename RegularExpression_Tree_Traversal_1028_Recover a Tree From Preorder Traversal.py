""" We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9. """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def preorder(self):
        ans, st = [], []
        while self or st:
            if self:
                ans.append(self.val)
                if self.right: st.append(self.right)
                self = self.left
            else:
                self = st.pop()
        return ans
    def inorder(self):
        ans, st = [], []
        while self or st:
            if self:
                st.append(self)
                self = self.left
            else:
                ans.append((p := st.pop()).val)
                self = p.right
        return ans
    def postorder(self):
        ans, st, pre = [], [], None
        while self or st:
            if self:
                st.append(self)
                self = self.left
            else:
                if not st[-1].right or st[-1].right == pre:
                    ans.append((pre := st.pop()).val)
                else:
                    self = st[-1].right
        return ans
    def levelOrder(self):
        ans = []
        q = [self]
        while q:
            node = q.pop(0)
            if not node: ans.append(None)
            else:
                ans.append(node.val)
                if node.left or node.right: 
                    q.append(node.left)
                    q.append(node.right)
        return ans


import re
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dummy = TreeNode(0)
        st = [(dummy, -1)]
        for d, x in re.findall(r'(-*)(\d+)', S):
            d, node = len(d), TreeNode(int(x))
            if d == st[-1][1] + 1: 
                st[-1][0].left = node
            else:
                while d < st[-1][1] + 1: st.pop() # stack, first pop unsatisfied ones
                st[-1][0].right = node
            st.append((node, d))
        return dummy.left

print(Solution().recoverFromPreorder("1-2-3").preorder()) #[1,2,3]
print(Solution().recoverFromPreorder("1-2-3").inorder()) #[2,1,3]
print(Solution().recoverFromPreorder("1-2-3").postorder()) #[2,3,1]

print(Solution().recoverFromPreorder("1-2--3--4-5--6--7").levelOrder()) #[1,2,5,3,4,6,7]
print(Solution().recoverFromPreorder("1-2--3---4-5--6---7").levelOrder()) #[1,2,5,3,null,6,null,4,null,7]
print(Solution().recoverFromPreorder("1-401--349---90--88").levelOrder()) #[1,401,null,349,88,90]
