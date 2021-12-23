# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.ans = 0
        self.targetSum = targetSum
        preVal = collections.defaultdict(int)
        preVal[0] = 1
        # dfs
        def dfs(preVal,s,node):
            if not node:
                return
            s += node.val
            #print(node.val,s,s - self.targetSum,preVal)
            if s - self.targetSum in preVal:
                self.ans += preVal[s - self.targetSum]
            preVal[s] += 1
            dfs(preVal,s,node.left)
            dfs(preVal,s,node.right)
            preVal[s] -= 1
        
        dfs(preVal,0,root)
        return self.ans