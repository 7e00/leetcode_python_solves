# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValid(self, root):
        if root.left == None and root.right == None:
            return (True, root.val, root.val)
        minval = root.val
        maxval = root.val
        if root.left:
            res = self.isValid(root.left)
            minval = res[1]
            if res[0] == False:
                return (False, minval, maxval)
            if res[2] >= root.val:
                return (False, minval, maxval)
        if root.right:
            res = self.isValid(root.right)
            maxval = res[2]
            if res[0] == False:
                return (False, minval, maxval)
            if res[1] <= root.val:
                return (False, minval, maxval)
        return (True, minval, maxval)
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root == None:
            return True
        return self.isValid(root)[0]