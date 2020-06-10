# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(r,left,right):
            if not r:
                return True
            if left < r.val < right:
                return isValid(r.left,left,r.val) and isValid(r.right,r.val,right)
            else:
                return False
        return isValid(root,float('-inf'),float('inf'))