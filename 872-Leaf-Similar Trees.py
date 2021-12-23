# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(r,v):
            if r.left:
                dfs(r.left,v)
            if r.right:
                dfs(r.right,v)
            if not r.left and not r.right:
                v.append(r.val)
        
        v1 = []
        v2 = []
        dfs(root1,v1)
        dfs(root2,v2)
        return v1 == v2