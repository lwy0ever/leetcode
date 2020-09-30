# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def ct(r,pre):  # 返回当前节点的累加值,此前的累加值为pre
            if not r:
                return pre
            pre = ct(r.right,pre)
            r.val += pre
            return ct(r.left,r.val)
        
        ct(root,0)
        return root