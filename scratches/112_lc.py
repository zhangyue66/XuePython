# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root,sum):
        if root is None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum

        else:
            #if root.left != None:
                answer = sum - root.val
                if self.hasPathSum(root,answer):
                    return True

            #if root.right != None:
                #answer = sum -root.val
                if self.hasPathSum(root,answer):
                    return True

                return False







