# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(pre,tn):
            if tn:
                p = (pre << 1) + tn.val
                if tn.left:
                    helper(p,tn.left)
                if tn.right:
                    helper(p,tn.right)
                if not tn.left and not tn.right:
                    self.ans += p
        helper(0,root)
        return self.ans