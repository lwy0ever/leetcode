# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def lca(root):
            if self.ans:    # 已有结果,不用再判断
                return False
            if not root:
                return False
            left = lca(root.left)
            if self.ans:    # 已有结果,不用再判断
                return False
            right = lca(root.right)
            if self.ans:    # 已有结果,不用再判断
                return False
            mid = (root == p) or (root == q)
            if mid + left + right == 2:
                self.ans = root
            return mid or left or right
        
        lca(root)
        return self.ans