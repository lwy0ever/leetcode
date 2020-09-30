# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.curVal = float('-inf')
        self.curCnt = 1
        self.maxCnt = 0
        
        def inorder(r):
            if not r:
                return
            inorder(r.left)
            if r.val == self.curVal:
                self.curCnt += 1
            else:
                self.curVal = r.val
                self.curCnt = 1
            if self.curCnt > self.maxCnt:
                self.maxCnt = self.curCnt
                self.ans = [self.curVal]
            elif self.curCnt == self.maxCnt:
                self.ans.append(self.curVal)
            inorder(r.right)
        inorder(root)
        return self.ans