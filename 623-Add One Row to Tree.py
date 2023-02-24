# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def addOne(r,level):
            if level > 1:
                if r.left:
                    addOne(r.left,level - 1)
                if r.right:
                    addOne(r.right,level - 1)
            else:
                tn = TreeNode(val)
                tn.left = r.left
                r.left = tn

                tn = TreeNode(val)
                tn.right = r.right
                r.right = tn
            
        if depth == 1:
            tn = TreeNode(val)
            tn.left = root
            return tn
        addOne(root,depth - 1)
        return root