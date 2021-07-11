# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root):

        yz = self.inorder(root)
        i,j = 0,len(yz)-1
        while i != j:
            if yz[i] == yz[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def inorder(self,root):
        check_list = []
        if root == None:
            root = TreeNode("null")
            return
        else:
            self.inorder(root.left)
            check_list.append(root.val)
            self.inorder(root.right)
        return check_list

    # def isSymmetric(self, root):
    #     if root is None:
    #         return True
    #     else:
    #         return self.isMirror(root.left,root.right)
    #
    #
    # def isMirror(self,left,right):
    #
    #     if left == None and right == None:
    #         return True
    #     elif left ==None or right == None:
    #         return False
    #     else:
    #
    #         if left.val == right.val:
    #             A_CONS = self.isMirror(left.left,right.right)
    #             B_CONS = self.isMirror(left.right,right.left)
    #             if A_CONS and B_CONS:
    #                 return True
    #
    #         return False

