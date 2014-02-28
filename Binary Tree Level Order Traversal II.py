# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        t = [[root.val]]
        layer = [root]
        while True:
            nlayer = []
            for node in layer:
                if node.left:
                    nlayer.append(node.left)
                if node.right:
                    nlayer.append(node.right)
            if len(nlayer) == 0:
                break
            t.append([node.val for node in nlayer])
            layer = nlayer
        return t[::-1]