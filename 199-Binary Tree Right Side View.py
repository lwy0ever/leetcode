# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        # dfs,其实bfs也行
        def dfs(root,depth):
            if root.left or root.right:
                nonlocal ans
                if len(ans) < depth + 1:
                    ans.append(None)
                if not ans[depth]:
                    if root.right:
                        ans[depth] = root.right.val
                    else:
                        ans[depth] = root.left.val
                if root.right:
                    dfs(root.right,depth + 1)
                if root.left:
                    dfs(root.left,depth + 1)
        
        if root:
            ans.append(root.val)
            dfs(root,1)
        return ans