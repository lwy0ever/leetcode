# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(r,op):  # op是二进制数,个位表示父节点是否偶数,十位表示祖父是否偶数
            if not r:
                return 0
            #print(r.val,op)
            ans = 0
            if r.val & 1 == 0:
                ans += dfs(r.left,(op << 1) + 1) + dfs(r.right,(op << 1) + 1)
            else:
                ans += dfs(r.left,(op << 1)) + dfs(r.right,(op << 1))
            if op & 2:
                return ans + r.val
            else:
                return ans

        return dfs(root,0)