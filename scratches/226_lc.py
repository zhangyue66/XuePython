# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if root is None:
            return
        if root.left == None and root.right == None:
            return root

        else:

            temp_node = TreeNode(999)

            temp_node = root.left
            root.left = root.right
            root.right = temp_node

            self.invertTree(root.left)
            self.invertTree(root.right)

            return root








