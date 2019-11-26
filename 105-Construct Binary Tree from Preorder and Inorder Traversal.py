# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        # preorder[0]是根节点
        root = TreeNode(preorder[0])
        # 在inorder中查找preorder[0],该位置将inorder分为左\右2个子树
        pos = inorder.index(preorder[0])
        # 分别构建左右子树
        root.left = self.buildTree(preorder[1:pos + 1],inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:],inorder[pos + 1:])
        
        return root