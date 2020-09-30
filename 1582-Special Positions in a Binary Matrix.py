class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        n = len(mat[0])
        rowSum = [sum(m) for m in mat]
        for c in range(n):
            row1 = -1   # 记录出现1的位置
            for r in range(m):
                if mat[r][c] == 1:
                    if row1 != -1:  # 第二次出现1
                        break
                    row1 = r
            else:
                # 出现且只在row1行出现了1次1
                if row1 != -1 and rowSum[row1] == 1:
                    ans += 1
        return ans