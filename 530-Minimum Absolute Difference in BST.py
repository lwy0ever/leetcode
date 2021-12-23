# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 中序遍历
        self.ans = float('inf')
        self.pre = float('-inf')
        def dfs(r): # r表示考虑当前的节点,pre为前一个数字
            if not r:
                return
            dfs(r.left)
            self.ans = min(self.ans,r.val - self.pre)
            self.pre = r.val
            dfs(r.right)
        dfs(root)
        return self.ans