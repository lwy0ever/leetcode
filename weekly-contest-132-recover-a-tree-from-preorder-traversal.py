# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        import re
        ind = 0
        n = len(S)
        
        def recover(level):
            cnt = 0
            nonlocal ind
            preIndex = ind
            while ind < n and S[ind] == '-':
                cnt += 1
                ind += 1
            if cnt != level:
                ind = preIndex
                return None
            g = re.search('^\d+',S[ind:])
            #print(g)
            val = int(g.group(0))
            ind += g.span(0)[1]
            #print(val,ind)
            tn = TreeNode(val)
            t1 = recover(level + 1)
            if t1:
                tn.left = t1
                t2 = recover(level + 1)
                if t2:
                    tn.right = t2
            return tn
        
        return recover(0)
            
            