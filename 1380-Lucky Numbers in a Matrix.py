class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        mins = []
        for i in range(n):
            mi = matrix[i][0]
            pos = (i,0)
            for j in range(1,m):
                if matrix[i][j] < mi:
                    pos = (i,j)
                    mi = matrix[i][j]
            mins.append(pos)
        for i,j in mins:
            ma = matrix[i][j]
            for l in range(n):
                if matrix[l][j] > ma:
                    break
            else:
                ans.append(ma)
        return ans