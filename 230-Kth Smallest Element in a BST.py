# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        # 中序遍历
        def dfs(root):
            if not root:
                return None
            r = dfs(root.left)
            if r != None:
                return r
            nonlocal cnt
            cnt += 1
            if cnt == k:
                return root.val
            r = dfs(root.right)
            if r != None:
                return r
        
        return dfs(root)