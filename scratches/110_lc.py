# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self,root):
        if root is None:
            return True
        else:
            left_tree_height = self.getHeight(root.left)
            right_tree_height = self.getHeight(root.right)
            return abs(left_tree_height-right_tree_height) <= 1 and \
                   self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self,root):
        if root is None:
            return 0
        else:
            return max(self.getHeight(root.left),self.getHeight(root.right))+1
