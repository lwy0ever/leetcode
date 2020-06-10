class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        ranges = [0,rows,0,cols]
        #print(ranges)
        ans = []
        while True:
            for i in range(ranges[2],ranges[3]):
                ans.append(matrix[ranges[0]][i])
            ranges[0] += 1
            if ranges[0] >= ranges[1]:
                break
            #print(ranges)
            for i in range(ranges[0],ranges[1]):
                ans.append(matrix[i][ranges[3] - 1])
            ranges[3] -= 1
            if ranges[2] >= ranges[3]:
                break
            #print(ranges)
            for i in range(ranges[3] - 1,ranges[2] - 1,-1):
                ans.append(matrix[ranges[1] - 1][i])
            ranges[1] -= 1
            if ranges[0] >= ranges[1]:
                break
            #print(ranges)
            for i in range(ranges[1] - 1,ranges[0] - 1,-1):
                ans.append(matrix[i][ranges[2]])
            ranges[2] += 1
            if ranges[2] >= ranges[3]:
                break
            #print(ranges)
        return ans