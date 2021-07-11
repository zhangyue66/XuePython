class Solution:
    def maxDepth(self,root):
        max_depth = -float("inf")
        count = 1
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

