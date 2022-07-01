# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 方法2:双指针
        left,right = root,root
        lstack,rstack = [root],[root]
        while left.left:
            left = left.left
            lstack.append(left)
        while right.right:
            right = right.right
            rstack.append(right)
        while left != right:
            s = left.val + right.val
            #print(left.val,right.val)
            if s == k:
                return True
            elif s < k:
                left = lstack.pop()
                node = left.right
                while node:
                    lstack.append(node)
                    node = node.left
            else:   # s > k
                right = rstack.pop()
                node = right.left
                while node:
                    rstack.append(node)
                    node = node.right
        return False

        # 方法1:dfs + hash
        '''
        self.s = set()
        def dfs(r,k):
            if not r:
                return False
            if k - r.val in self.s:
                return True
            self.s.add(r.val)
            #print(self.s)
            return dfs(r.left,k) or dfs(r.right,k)
        
        return dfs(root,k)
        '''