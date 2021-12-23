# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # method 2:直接在树结构上修改
        ans = TreeNode(-1)
        cur = ans
        def LDR(r):
            nonlocal cur
            if not r:
                return
            #print(r.val)
            LDR(r.left)
            cur.right = r
            r.left = None
            cur = cur.right
            LDR(r.right)
        LDR(root)
        return ans.right

        # method 1:先转为list,再构建link
        l = list()
        def LDR(r):
            if not r:
                return
            LDR(r.left)
            l.append(r.val)
            LDR(r.right)
        LDR(root)
        ans = TreeNode(-1)
        cur = ans
        for v in l:
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right