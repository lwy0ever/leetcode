# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(r,mi,ma):
            if r:
                if r.val <= mi or r.val >= ma:
                    return False
                else:
                    return dfs(r.left,mi,r.val) and dfs(r.right,r.val,ma)
            return True
        
        if root:
            return dfs(root.left,float('-inf'),root.val) and dfs(root.right,root.val,float('inf'))
        else:
            return True