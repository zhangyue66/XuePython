# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self,root):

        if root is None:
            return 0
        else:
            if root.left and root.right:
                return min(self.minDepth(root.left),self.minDepth(root.right))

            elif root.left and root.right is None:
                return self.minDepth(root.right)
            else:
                return self.minDepth(root.left)









