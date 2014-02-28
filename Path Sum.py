# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPath(self, root, sum, nowsum):
        if root == None:
            return sum == nowsum
        if root.left == None and root.right == None:
            return sum == nowsum+root.val
        res = False
        if root.left != None:
            res = self.hasPath(root.left, sum, nowsum+root.val)
        if not res and root.right != None:
            res = self.hasPath(root.right, sum, nowsum+root.val)
        return res
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        return self.hasPath(root, sum, 0)