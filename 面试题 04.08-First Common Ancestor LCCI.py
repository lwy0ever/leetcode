# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 函数返回以root为根的树,包含p或者q的节点,如果不含,则返回None
        if not root or root == p or root == q:
            return root
        # 由于p,q均存在于给定的二叉树
        # 如果root.left不包含p或q,则目标节点必在root.right的子树
        # 如果root.right不包含p或q,则目标节点必在root.left的子树
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        # root.left和root.right都含p或q,则返回root
        return root