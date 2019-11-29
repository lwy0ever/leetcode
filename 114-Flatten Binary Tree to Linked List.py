# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 非递归
        while root:
            # 将左子树的最右节点,指向右子树的根节点
            # 将root.right指向root.left,root.left置空
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            # 指针移动到root.right
            root = root.right

        # 递归
        '''
        if not root:
            return
        # root.left,root.right都变为链表
        self.flatten(root.left)
        self.flatten(root.right)
        # root.left的tail指向root.right,root.right指向root.left
        if root.left:
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.right = root.left
            root.left = None
        '''