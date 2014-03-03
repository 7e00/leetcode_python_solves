# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self, root, path):
        if root.left != None:
            self.postorder(root.left, path)
        if root.right != None:
            self.postorder(root.right, path)
        path.append(root.val)
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []
        path = []
        self.postorder(root, path)
        return path