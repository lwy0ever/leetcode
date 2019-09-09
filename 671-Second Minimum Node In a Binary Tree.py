# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = deque([float('inf')] * 2,maxlen = 2)
        def dfs(root):
            nonlocal ans
            if root:
                if root.val < ans[0]:
                    ans.appendleft(root.val)
                if root.val > ans[0] and root.val < ans[1]:
                    ans[1] = root.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return -1 if ans[1] == float('inf') else ans[1]