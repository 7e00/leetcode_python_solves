# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bst(self, num, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(num[l])
        mid = (l+r)//2
        root = TreeNode(num[mid])
        root.left = self.bst(num, l, mid-1)
        root.right = self.bst(num, mid+1, r)
        return root
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.bst(num, 0, len(num)-1)