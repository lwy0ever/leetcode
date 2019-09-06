# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        ans = []

        def dfs(root, fatherNotDeleted):
            if not root: return None
            deleted = root.val in s
            if fatherNotDeleted and not deleted:
                ans.append(root)
            root.left = dfs(root.left, deleted)
            root.right = dfs(root.right, deleted)
            return None if deleted else root
        dfs(root, True)
        return ans        