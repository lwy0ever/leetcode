class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 和方法1一样,尝试节约点空间
        m = len(mat)
        n = len(mat[0])
        # 向右上的,起点分别是(0,0),(1,0),(2,0)...(m - 1,0),(m - 1,1),(m - 1,2)...(m - 1,n - 1)
        # 向左下的,起点分别是(0,0),(0,1),(0,2)...(0,n - 1),(1,n - 1),(2,n - 1)...(m - 1,n - 1)
        #print(len(rightUp),len(leftDown))
        ans = []
        for i in range(m + n - 1):
            if i & 1 == 0:  # 方向,右上
                r = i if i < m else m - 1
                c = 0 if i < m else i - m + 1
                #print(r,c)
                while r >= 0 and c < n:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
            else:   # 方向,左下
                r = 0 if i < n else i - n + 1
                c = i if i < n else n - 1
                #print(r,c)
                while r < m and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
        return ans

        # 方法1:
        '''
        m = len(mat)
        n = len(mat[0])
        # 向右上的,起点分别是(0,0),(1,0),(2,0)...(m - 1,0),(m - 1,1),(m - 1,2)...(m - 1,n - 1)
        # 向左下的,起点分别是(0,0),(0,1),(0,2)...(0,n - 1),(1,n - 1),(2,n - 1)...(m - 1,n - 1)
        rightUp = [(i,0) for i in range(m)] + [(m - 1,i) for i in range(1,n)]
        leftDown = [(0,i) for i in range(n)] + [(i,n - 1) for i in range(1,m)]
        #print(len(rightUp),len(leftDown))
        ans = []
        for i in range(m + n - 1):
            if i & 1 == 0:  # 方向,右上
                r,c = rightUp[i]
                while r >= 0 and c < n:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
            else:   # 方向,左下
                r,c = leftDown[i]
                while r < m and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
        return ans
        '''