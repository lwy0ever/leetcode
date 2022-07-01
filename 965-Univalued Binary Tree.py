# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def helper(val,tn): # 如果tn是值为val的单值二叉树,则返回true,否则返回false
            if not tn:
                return True
            if tn.val == val:
                return helper(val,tn.left) and helper(val,tn.right)
            else:
                return False
        
        return helper(root.val,root.left) and helper(root.val,root.right) if root else True