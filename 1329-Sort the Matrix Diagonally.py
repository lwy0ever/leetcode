class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0] * m for _ in range(n)]
        for c in range(m - 1,-1,-1):
            if c > 0:
                endRow = 1
            else:
                endRow = n
            for r in range(endRow):
                arr = []
                x,y = r,c
                while x < n and y < m:
                    bisect.insort(arr,mat[x][y])
                    x += 1
                    y += 1
                #arr.sort()
                #print(arr)
                x,y = r,c
                i = 0
                while x < n and y < m:
                    ans[x][y] = arr[i]
                    x += 1
                    y += 1
                    i += 1
        return ans