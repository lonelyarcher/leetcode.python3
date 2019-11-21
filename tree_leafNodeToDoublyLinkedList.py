"""
Extract Leaves of a Binary Tree in a Doubly Linked List
Given a Binary Tree, extract all leaves of it in a Doubly Linked List (DLL). Note that the DLL need to be created in-place. Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers are different. In DLL, left means previous pointer and right means next pointer.

Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
7<->8<->5<->9<->10

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):

    def convertLeafToDoublyLinkedList(self, root):
        prev = None
        def convert(root): # postorder 
            nonlocal prev
            if root:
                convert(root.right)
                convert(root.left)
                if not root.right and not root.left:
                    if prev:
                        root.right = prev
                        prev.left = root
                    prev = root
                else:
                    if root.right and not root.right.right and not root.right.left:
                        root.right == None
                    if root.left and not root.left.right and not root.left.left:
                        root.left = None
                
        convert(root)
        return prev

#Test
s = Solution()
root = TreeNode(0)
l = TreeNode(1)
r = TreeNode(2)
ll = TreeNode(3)
rr = TreeNode(5)
rl = TreeNode(4)
root.left = l
root.right = r
l.left = ll
r.left = rl
r.right = rr
head = s.convertLeafToDoublyLinkedList(root)
while head:
    print(head.val)
    head = head.right



 
