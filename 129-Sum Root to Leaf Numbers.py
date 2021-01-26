# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(pre,r):
            p = pre * 10 + r.val
            if r.left or r.right:
                if r.left:
                    dfs(p,r.left)
                if r.right:
                    dfs(p,r.right)
            else:
                self.ans += p
        if root:
            dfs(0,root)
        return self.ans