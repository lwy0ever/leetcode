# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: # 都是None
            return True
        if not s or not t:  # 其中一个是None
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSame(self,a,b):
        if not a and not b: # 都是None
            return True
        if not a or not b:  # 其中一个是None
            return False
        return a.val == b.val and self.isSame(a.left,b.left) and self.isSame(a.right,b.right)
