# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dc(root):
            if not root:
                return 0,0  # 此节点贡献/需求的coin数量，此节点以下部分交换的次数
            l,nl = dc(root.left)
            r,nr = dc(root.right)
            return root.val + l + r - 1,abs(l) + nl + abs(r) + nr
        _,n = dc(root)
        return n
        '''
        self.ans = 0

        def dc(root):
            if not root:
                return 0
            l = dc(root.left)
            r = dc(root.right)
            self.ans += abs(l) + abs(r)
            return root.val + l + r - 1
        
        dc(root)
        return self.ans
        '''