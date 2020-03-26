# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.ans = 0

        def ll(root,isLeft):
            if root.left is None and root.right is None:
                if isLeft:
                    self.ans += root.val
            else:
                if root.left:
                    ll(root.left,True)
                if root.right:
                    ll(root.right,False)
        
        ll(root,False)
        return self.ans