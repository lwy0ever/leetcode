# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        elif t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
        '''
        def dfs(n1,n2):
            if n1.left:
                if n2.left:
                    n1.left.val += n2.left.val
                    dfs(n1.left,n2.left)
            else:
                if n2.left:
                    n1.left = n2.left
            if n1.right:
                if n2.right:
                    n1.right.val += n2.right.val
                    dfs(n1.right,n2.right)
            else:
                if n2.right:
                    n1.right = n2.right
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        dfs(t1,t2)
        return t1
        '''        