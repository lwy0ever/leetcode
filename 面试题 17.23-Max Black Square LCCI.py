class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        rM = [[0] * n for _ in range(n)]    # rM[i][j]表示以(i,j)为起点,向右延申的黑色(0)长度
        cM = [[0] * n for _ in range(n)]    # cM[i][j]表示以(i,j)为起点,向下延申的黑色(0)长度
        for i in range(n):
            l = 0
            for j in range(n - 1,-1,-1):
                if matrix[i][j] == 0:
                    l += 1
                else:
                    l = 0
                rM[i][j] = l
        for i in range(n):
            l = 0
            for j in range(n - 1,-1,-1):
                if matrix[j][i] == 0:
                    l += 1
                else:
                    l = 0
                cM[j][i] = l
        #print(rM)
        #print(cM)
        ans = []
        for r in range(n):
            for c in range(n):
                maxSize = min(rM[r][c],cM[r][c])
                mx = ans[2] if ans else 1
                for size in range(maxSize,mx - 1,-1):
                    if rM[r + size - 1][c] >= size and cM[r][c + size - 1] >= size:
                        if not ans or (size > ans[2]) or (size == ans[2] and r < ans[0]) or (size == ans[2] and r == ans[0] and c < ans[1]):
                            ans = [r,c,size]
        return ans
        '''
        for size in range(n,0,-1):
            for r in range(n - size + 1):
                for c in range(n - size + 1):
                    if rM[r][c] >= size and rM[r + size - 1][c] >= size and cM[r][c] >= size and cM[r][c + size - 1] >= size:
                        return [r,c,size]
        return []
        '''