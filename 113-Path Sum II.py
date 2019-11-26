# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root,arr,s):
            if root == None:
                return
            s -= root.val
            if root.left == None and root.right == None:
                if s == 0:
                    ans.append(arr + [root.val])
            dfs(root.left,arr + [root.val],s)
            dfs(root.right,arr + [root.val],s)
        
        ans = []
        dfs(root,[],sum)
        return ans