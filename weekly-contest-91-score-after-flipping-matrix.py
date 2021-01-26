class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 先移动行,使得第一个数为1
        # 之后统计第2列的0和1的数量,如果0多余1,则移动
        # 之后统计第3列的0和1的数量,如果0多余1,则移动
        # ...
        # 之后统计第n列的0和1的数量,如果0多余1,则移动
        m = len(A)
        n = len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1
        for i in range(1,n):
            cnt0 = 0
            for j in range(m):
                if A[j][i] == 0:
                    cnt0 += 1
            if cnt0 > m // 2:
                for j in range(m):
                    A[j][i] ^= 1
        #print(A)
        ans = 0
        for i in range(m):
            s = 0
            for j in range(n):
                s = (s << 1) + A[i][j]
            ans += s
        return ans