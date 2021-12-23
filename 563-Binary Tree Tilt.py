# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        
        # dfs
        def dfs(n): # 求节点n的
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            self.ans += abs(l - r)
            return n.val + l + r
        
        dfs(root)
        return self.ans