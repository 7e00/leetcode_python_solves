# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        node = TreeNode(postorder[len(postorder)-1])
        for i in range(len(inorder)):
            if inorder[i] == node.val:
                break
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
        return node