# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def path(root,need):
            res = 0
            nn = [need[0]]
            for n in need:
                if root.val == n:
                    res += 1
                nn.append(n - root.val)
            if root.left:
                res += path(root.left,nn)
            if root.right:
                res += path(root.right,nn)
            return res
                            
        #need = defaultdict(int)
        #need[sum] += 1
        need = [sum]
        if root:
            return path(root,need)
        else:
            return 0