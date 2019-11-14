class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        s = [[0] * m for _ in range(n)]
        for r,c in indices:
            for i in range(m):
                s[r][i] += 1
            for i in range(n):
                s[i][c] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if s[i][j] & 1 == 1:
                    ans += 1
        return ans