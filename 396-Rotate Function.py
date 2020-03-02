class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        if n <= 1:
            return 0
        # 当知道F(i - 1)后,我们求F(i)时,实际上是先减去n*最后一个数,再加上原数组排除最后一数的数组和,即F(i) = F(i - 1) + sum(A) - A[-i] * n
        Fx = 0
        for ind,x in enumerate(A):
            Fx += x * ind
        ans = Fx
        _sum = sum(A)
        for i in range(1,n):
            Fx = Fx + _sum - A[- i] * n
            ans = max(ans,Fx)
        return ans