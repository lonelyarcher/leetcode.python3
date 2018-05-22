class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):

    def inorder(self, root): 
        # from root, go left, put root into stack
        # when left to the end, no root then pop stack
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right

        return res


    def preorder(self, root): 
        # from root, travel root, put right into stack
        # go left, when end pop the stack to right node.
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return res

    def postorder(self, root): 
        # from root, go left, put the root into stack.
        # keep record of last visit (in case don't repeat going right when root back from right)
        # when left to end, peek the stack to go to its right if it has right and not visited ( right != pre) 
        # if no right or already visit right, visit the root and record it as pre.
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        pre = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else: 
                if stack[-1].right and pre != stack[-1].right:
                    root = stack[-1].right
                else:
                    pre = stack.pop()
                    res.append(pre.val)
        return res

# Test
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(0)
e = TreeNode(2.5)
b.left, b.right = a, c
a.left = d
c.left = e
s = Solution()
ans = s.inorder(b)
print(ans)
print(s.preorder(b))
print(s.postorder(b))

