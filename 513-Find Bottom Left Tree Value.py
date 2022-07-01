# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = None
        maxLevel = -1
        # dfs
        def dfs(tn,level):
            nonlocal ans,maxLevel
            if tn.left:
                dfs(tn.left,level + 1)
            if tn.right:
                dfs(tn.right,level + 1)
            if level > maxLevel:
                ans = tn.val
                maxLevel = level
        
        dfs(root,0)
        return ans