# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(r):
            if r:
                return [r.val] + dfs(r.left) + dfs(r.right)
            return []
        x = dfs(root1)
        y = dfs(root2)
        s1 = set(x)
        for i in y:
            if target - i in s1:
                return True
        return False