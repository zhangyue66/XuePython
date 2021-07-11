# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self,nums):
        if len(nums) == 0:
            return
        else:
            mid = len(nums)//2
            left = nums[::mid]
            right = nums[mid+1::]

            root = TreeNode(nums[mid])

            root.left = self.sortedArrayToBST(left)
            root.right = self.sortedArrayToBST(right)

            return root