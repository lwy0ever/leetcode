class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        n = len(A)
        if n <= 2:
            return 0
        p = 0   # 等差数列起始位置
        step = float('inf')
        for i in range(1,n):
            if A[i] - A[i - 1] != step:
                if i - 1 - p >= 2:
                    #print(i,p,step)
                    ans += (i - p - 2 + 1) * (i - p - 2) // 2
                p = i - 1
                step = A[i] - A[i - 1]
            #print(i,p,step)
        #print(p,i,step)
        #print(ans)
        if i - p >= 2:
            ans += (i - p - 1 + 1) * (i - p - 1) // 2
        return ans