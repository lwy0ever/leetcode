class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 对于某个点(i,j),找到rowSum[i]和colSum[j]的小值,放置在此处
        # 然后更新rowSum[i]和colSum[j]
        m = len(rowSum)
        n = len(colSum)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = min(rowSum[i],colSum[j])
                ans[i][j] = a
                rowSum[i] -= a
                colSum[j] -= a
        return ans