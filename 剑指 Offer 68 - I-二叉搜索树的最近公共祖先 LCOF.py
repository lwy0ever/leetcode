# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 设最近公共祖先为ans
        # 令p.val < q.val
        # 则ans.val >= p.val and ans.val <= q.val
        if p.val > q.val:
            p,q = q,p
        r = root
        while True:
            if r.val >= p.val and r.val <= q.val:
                return r
            if r.val > q.val:
                r = r.left
            else:
                r = r.right