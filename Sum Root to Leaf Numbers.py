# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNode(self, node, val):
        res = 0;
        if node.left == None and node.right == None:
            return val*10+node.val
        if node.left != None:
            res += self.sumNode(node.left, val*10+node.val)
        if node.right != None:
            res += self.sumNode(node.right, val*10+node.val)
        return res
    def sumNumbers(self, root):
        if root == None:
            return 0
        return self.sumNode(root, 0)