# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # 由于distance <= 10,每个叶子节点返回其深度1
        # 用arrayLeft记录每个节点左子树的叶子深度的个数,arrayLeft[i]表示深度为i + 1的叶子节点数
        ans = 0
        def dfs(tn):
            if not tn.left and not tn.right:
                arr = [0] * 10
                arr[0] = 1
                return arr
            if tn.left:
                arrayLeft = dfs(tn.left)
            else:
                arrayLeft = [0] * 10
            if tn.right:
                arrayRight = dfs(tn.right)
            else:
                arrayRight = [0] * 10
            for l in range(10):
                for r in range(10):
                    if l + r + 2 <= distance:
                        nonlocal ans
                        ans += arrayLeft[l] * arrayRight[r]
            arr = [0] * 10
            for i in range(1,10):
                arr[i] = arrayLeft[i - 1] + arrayRight[i - 1]
            return arr
        dfs(root)
        return ans