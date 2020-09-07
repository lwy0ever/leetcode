class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n))
        if n & 1:   # 奇数,去掉中间重复点
            ans -= mat[n // 2][n // 2]
        return ans