# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def isSame(root,val):
            if root:
                if root.val == val:
                    return isSame(root.left,val) and isSame(root.right,val) 
                else:
                    return False
            else:
                return True
        
        if root:
            return isSame(root.left,root.val) and isSame(root.right,root.val) 
        else:
            return True