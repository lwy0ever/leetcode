# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def addOne(r,level):
            if level > 1:
                if r.left:
                    addOne(r.left,level - 1)
                if r.right:
                    addOne(r.right,level - 1)
            else:
                tn = TreeNode(v)
                tn.left = r.left
                r.left = tn

                tn = TreeNode(v)
                tn.right = r.right
                r.right = tn
            
        if d == 1:
            tn = TreeNode(v)
            tn.left = root
            return tn
        addOne(root,d - 1)
        return root