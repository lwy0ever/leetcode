# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # dfs
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            if left == -1:
                return -1
            right = depth(root.right)
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return max(left,right) + 1
            else:
                return -1
        if depth(root) == -1:
            return False
        else:
            return True
        '''
        def checkBalanced(root):
            if not root:
                return True,0
            checkLeft,leftDepth = checkBalanced(root.left)
            checkRight,rightDepth = checkBalanced(root.right)
            return checkLeft and checkRight and abs(leftDepth - rightDepth) <= 1,max(leftDepth,rightDepth) + 1

        c,d = checkBalanced(root)
        return c
        '''