# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        # 某个树,总时间a,最大并行时间b,则最终运行时间 = 单独运行时间 + 并行时间 = (a - 2b) + b = a - b
        # 某个树
        # 左子树,总时间a,最大并行时间b
        # 右子树,总时间c,最大并行时间d
        # 设a >= c
        # 如果a - 2b <= c,则应该左子树先并行a - c的任务,用时((a - c)/2),然后再和右子树一起并行c时间,总并行用时(a + c) / 2
        # 如果a - 2b > c,那么剩余a - 2b - c的任务无法左右树并行,所以并行时间最大为 = b + (a - (a - 2b - c) + c) / 2 = b + c
        def dfs(r): # 返回该树的总时间,最大并行时间
            if not r:
                return 0,0
            a,b = dfs(r.left)
            c,d = dfs(r.right)
            if a < c:
                a,b,c,d = c,d,a,b
            if a - b * 2 <= c:
                return r.val + a + c,(a + c) / 2
            else:
                return r.val + a + c,b + c
        a,b = dfs(root)
        return a - b