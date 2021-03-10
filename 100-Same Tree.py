# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p,q):
            if bool(p) != bool(q):  # 一个为None，一个非None
                return False
            if not p:   # 两个都是None
                return True
            if p.val != q.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)