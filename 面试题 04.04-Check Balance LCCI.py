# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(r):
            if not r:
                return 0,True
            l,isL = depth(r.left)
            r,isR = depth(r.right)
            return max(l + 1,r + 1),(abs(l - r) <= 1 and isL and isR)
        return depth(root)[1]
        