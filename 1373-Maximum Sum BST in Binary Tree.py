# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def r(root):    # 返回3个值:键值和,下界,上界
            if not root:    # 父节点是叶子节点,符合BST
                return 0,float('inf'),float('-inf') # 最小值=inf,最大值=-inf,这样以父节点形成的二叉树是BST
            s1,left1,right1 = r(root.left)
            s2,left2,right2 = r(root.right)
            if right1 < root.val < left2:
                self.m = max(self.m,s1 + root.val + s2)
                return s1 + root.val + s2,min(root.val,left1),max(root.val,right2)
            else:
                return 0,float('-inf'),float('inf')

        self.m = 0
        r(root)
        return self.m