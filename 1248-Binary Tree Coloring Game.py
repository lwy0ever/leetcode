# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # 点x将树分为3个部分：左子树、右子树、父节点及相关子树
        # 如果3个部分中有一部分的节点数大于n // 2 + 1，则可以赢
        # step1: 找到n节点:tn
        vd = [root]
        while vd:
            tn = vd.pop()
            if tn.val == x:
                break
            if tn.left:
                vd.append(tn.left)
            if tn.right:
                vd.append(tn.right)
        # step2:遍历tn的左树
        vd = []
        l = 0
        if tn.left:
            vd.append(tn.left)
            l += 1
        while vd:
            p = vd.pop()
            if p.left:
                vd.append(p.left)
                l += 1
            if p.right:
                vd.append(p.right)
                l += 1
        #print(l)
        if l >= n // 2 + 1:
            return True
        # step2:遍历tn的右树
        vd = []
        r = 0
        if tn.right:
            vd.append(tn.right)
            r += 1
        while vd:
            p = vd.pop()
            if p.left:
                vd.append(p.left)
                r += 1
            if p.right:
                vd.append(p.right)
                r += 1
        #print(r)
        if r >= n // 2 + 1:
            return True
        if (n - l - r - 1) >= n // 2 + 1:
            return True
        return False

            
        
        
        