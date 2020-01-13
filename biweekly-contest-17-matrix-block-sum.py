class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + mat[i - 1][j - 1]
        #print(pre)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rMin = max(i - K,0)
                rMax = min(i + K,m - 1)
                cMin = max(j - K,0)
                cMax = min(j + K,n - 1)
                ans[i][j] = pre[rMax + 1][cMax + 1] - pre[rMax + 1][cMin] - pre[rMin][cMax + 1] + pre[rMin][cMin]
        return ans