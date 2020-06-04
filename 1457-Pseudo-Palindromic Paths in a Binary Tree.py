# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(r,mask):
            if r.left or r.right:   # 不是叶子节点
                if r.left:
                    dfs(r.left,mask ^ 1 << (r.val - 1))
                if r.right:
                    dfs(r.right,mask ^ 1 << (r.val - 1))
            else:   # 叶子节点
                t = mask ^ 1 << (r.val - 1)
                if t in goodMask:
                    self.ans += 1

        # 由于只有1-9共9种数字,使用二进制形式记录数字出现的次数(奇数/偶数)
        goodMask = [0]
        for i in range(9):
            goodMask.append(1 << i)
        self.ans = 0
        dfs(root,0)
        return self.ans