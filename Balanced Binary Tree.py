# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def depthAndBalance(self, root):
        if root == None:
            return (0,True)
        ld,lb = self.depthAndBalance(root.left)
        rd,rb = self.depthAndBalance(root.right)
        return (max(ld,rd)+1,lb and rb and abs(ld-rd)<=1)
    def isBalanced(self, root):
        return self.depthAndBalance(root)[1]