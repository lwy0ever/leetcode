# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        '''
        def isMirror(l,r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            return l.val == r.val and isMirror(l.left,r.right) and isMirror(l.right,r.left)

        return isMirror(root.left,root.right) if root else True
        '''

        # 迭代
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        return True