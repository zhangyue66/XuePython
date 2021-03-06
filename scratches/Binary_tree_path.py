# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = []

        def dfs(node,path,ans):
            if node is None:
                return
            else:
                if node.left is None and node.right is None:
                    path.append(node.val)
                    ans.append(path)

                if node.left:
                    #path.append(node.val)
                    dfs(node.left,path+[node.val],ans)
                if node.right:
                    #path.append(node.val)
                    dfs(node.right,path+[node.val],ans)


        dfs(root,[],ans)

        return ans