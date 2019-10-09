# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for po in preorder[1:]:
            t = root
            while True:
                if po < t.val:
                    if t.left:
                        t = t.left
                    else:
                        t.left = TreeNode(po)
                        break
                else:
                    if t.right:
                        t = t.right
                    else:
                        t.right = TreeNode(po)
                        break
        return root