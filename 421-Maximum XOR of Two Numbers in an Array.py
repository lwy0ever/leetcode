class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        cols = len(bin(max(nums))) - 2
        rows = len(nums)
        # 二进制化
        bits = [[(n >> i) & 1 for i in range(cols)][::-1] for n in nums]
        #print(bits)
        # 形成一个类似于二叉树的结构
        tr = {0:{}}
        for row in bits:
            t = tr[0]
            for c in row:
                if c in t:
                    t = t[c]
                else:
                    t[c] = {}
                    t = t[c]
        #print(tr)
        def t(A,B,col,maxNow):
            #print(A,B,col,maxNow)
            if col < 0:
                nonlocal ans
                ans = max(ans,maxNow)
                return
            if 0 in A and 1 in B:
                maxNow |= (1 << col)
                t(A[0],B[1],col - 1,maxNow)
            if 1 in A and 0 in B:
                maxNow |= (1 << col)
                t(A[1],B[0],col - 1,maxNow)
            if 0 not in A and 0 not in B:
                t(A[1],B[1],col - 1,maxNow)
            if 1 not in A and 1 not in B:
                t(A[0],B[0],col - 1,maxNow)
            
        ans = 0
        tA = tr[0]
        tB = tr[0]
        t(tA,tB,cols - 1,0)
        return ans