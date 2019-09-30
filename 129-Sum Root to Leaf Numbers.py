# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0        
        def dfs(tn,pre):
            if not tn:
                return
            if not tn.left and not tn.right:
                nonlocal ans
                ans += pre * 10 + tn.val
                return
            pre = pre * 10 + tn.val
            dfs(tn.left,pre)
            dfs(tn.right,pre)
        dfs(root,0)
        return ans