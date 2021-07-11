# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, item):
#         self.val = item
#         self.left = None
#         self.right = None
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def add(self,item):
#         node = TreeNode(item)
#
#         if self.root == None:
#             self.root = node
#             return
#         else:
#             queue = [self.root]
#             while queue is not None:
#                 cur_node = queue.pop(0)
#                 pass

class Solution:
    def isSameTree(self,p,q):

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                    return True
                return False

