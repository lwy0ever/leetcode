# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 返回两个数据
        # 1,行窃这个根节点可以得到的最大金额
        # 2,不行窃这个根节点可以得到的最大金额
        def dfs(tn):
            if not tn:
                return 0,0
            l = dfs(tn.left)
            r = dfs(tn.right)
            return tn.val + l[1] + r[1],max(l) + max(r)
        
        return max(dfs(root))