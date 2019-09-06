# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float('-inf')
        
        def dfs(root):
            nonlocal ans
            if not root:
                return float('-inf')
            l = dfs(root.left)
            r = dfs(root.right)
            #print(root.val,l,r)
            ans = max(ans,l + root.val + r,l,r)
            return max(root.val + l,root.val + r,root.val)
        
        r = dfs(root)
        ans = max(ans,r)
        return ans