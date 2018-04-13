# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s1 = {None: 0} # rob current node
        s2 = {None: 0} # not rob current node
        return max(self.rob1(root, s1, s2), self.rob2(root, s1, s2))

    def rob1(self, root, s1, s2): # rob current node
        if root not in s1:
            s1[root] = self.rob2(root.left, s1, s2) + self.rob2(root.right, s1, s2) + root.val
        return s1[root]   

    def rob2(self, root, s1, s2): # not rob current node
        if root not in s2:
            s2[root] = max(self.rob1(root.left, s1, s2), self.rob2(root.left, s1, s2)) + max(self.rob1(root.right, s1, s2), self.rob2(root.right, s1, s2))
        return s2[root]


    def rob_bottom_up_with_dual_return(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root): # return [] 0: not rob root, 1: rob root 
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            return [max(left[0], left[1]) + max(right[0], right[1]), left[0] + right[0] + root.val]
        ret = helper(root) 
        return max(ret[0], ret[1])
    

s = Solution()
print(s.rob(None))
       