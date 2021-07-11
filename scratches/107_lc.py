# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self,root):
        if root is None:
            return []
        else:

            queue = [root] # use queue to do breath traversal
            answer = [] # answer

            while queue:
                #cur_node = queue.pop(0)
                next = []
                vals = []
                for node in queue:
                    vals.append(node.val)
                    if node.left is not None:
                        next.append(node.left)
                    if node.right is not None:
                        next.append(node.right)
                queue = next
                answer.append(vals)


        return answer[::-1]








