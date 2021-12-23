class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * (n + 1)
        vals = []
        for i in range(m):
            newRow = [0] * (n + 1)
            for j in range(n):
                newRow[j + 1] = newRow[j] ^ matrix[i][j]
                row[j + 1] = newRow[j + 1] ^ row[j + 1]
                vals.append(row[j + 1])
            #print(row,newRow)
        #print(vals)
        vals.sort()
        return vals[-k]
                