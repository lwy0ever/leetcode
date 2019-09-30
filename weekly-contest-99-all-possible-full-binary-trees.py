# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    all = {0:[],1:[TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.all:
            ans = []
            for left in range(1,N,2):
                right = N - 1 - left
                for leftPossible in self.allPossibleFBT(left):
                    for rightPossible in self.allPossibleFBT(right):
                        node = TreeNode(0)
                        node.left = leftPossible
                        node.right = rightPossible
                        ans.append(node)
                self.all[N] = ans
        return self.all[N]
        
        