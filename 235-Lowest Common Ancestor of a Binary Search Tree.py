# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 设p<q
        # 如果p和q有一个最近的公共祖先root,则p.val <= root.val and q.val >= root.val
        # 当p和q同时小于/大于root.val的时候,说明不是最近的公共祖先,需要向下层寻找
        if p.val > q.val:
            p,q = q,p
        while True:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root