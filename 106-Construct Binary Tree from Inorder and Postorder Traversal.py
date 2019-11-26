# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 与105题类似,postorder[-1]是根节点
        if len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:pos],postorder[:pos])
        root.right = self.buildTree(inorder[pos + 1:],postorder[pos:-1])
        
        return root