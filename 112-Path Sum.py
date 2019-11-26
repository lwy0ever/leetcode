# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        sum -= root.val
        if root.left == None and root.right == None:
            return sum == 0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        '''
        def dfs(root,presum):
            if root == None:
                return False
            s = presum + root.val
            if root.left == None and root.right == None:
                return s == sum
            return dfs(root.left,s) or dfs(root.right,s)
        
        return dfs(root,0) if root else False
        '''