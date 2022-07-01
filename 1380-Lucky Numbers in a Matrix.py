class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        maxInCol = [0] * n  # 表示第i列的最大值所在的行
        minInRow = [float('inf')] * m   # 表示第i行的最大值
        for c in range(n):
            for r in range(1,m):
                if matrix[r][c] > matrix[maxInCol[c]][c]:
                    maxInCol[c] = r
                #print(maxInCol)
            minInRow[maxInCol[c]] = min(minInRow[maxInCol[c]],matrix[maxInCol[c]][c])
        ans = []
        for r in range(m):
            minInRowR = min(matrix[r])
            if minInRowR == minInRow[r]:
                ans.append(minInRowR)
        return ans