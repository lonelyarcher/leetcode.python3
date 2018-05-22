'''
297 Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or transmitted
across a network connection link to be reconstructed later in the same or another
computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work. You just
need to ensure that a binary tree can be serialized to a string and this string can
be deserialized to the original tree structure.
   1
  / \
 2   3
    / \
   4   5
Convert to [1 2 # # 3 4 # # 5 # #] and then back the tree
思路： 用preorder traversal 然后用#来代表None。 这样在造树的时候。就可以停
止在正确的位置。
'''
# Preorder by recursion is easiest way to implement. deserialize from a list, one by one use recursion helper.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:    
    def serialize(self, root):
        if not root: return '# '
        res = ''
        if root:
            res += str(root.val) + ' '
            res += self.serialize(root.left)
            res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        data = data.split()
        def helper():
            tmp = data.pop(0)
            if tmp == '#': return None
            root = TreeNode(int(tmp))
            root.left = helper()
            root.right = helper()
            return root
        root = helper()
        return root
    

# Test
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
codec = Codec()
ans = codec.serialize(a)
print(ans)
root = codec.deserialize(ans)
print(root.val, root.left.val, root.right.val, root.right.left.val, root.right.right.val)
