class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def inorder(self, root):
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
                node = stack.pop()
                
                root = node.right

        return res

# Test
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(0)
e = TreeNode(2.5)
b.left, b.right = a, c
a.right = d
c.left = e
s = Solution()
ans = s.inorder(b)
print(ans)

