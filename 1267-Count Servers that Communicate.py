class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        stack = set()
        for i in range(n):
            cnt = 0
            s = []
            for j in range(m):
                if grid[i][j] == 1:
                    s.append(j)
                    cnt += 1
                    ans += 1
            if cnt == 1:
                stack.add((i,s[0]))
        for x,y in stack:
            cnt = 0
            for i in range(n):
                if grid[i][y] == 1:
                    cnt += 1
            if cnt == 1:
                ans -= 1
        return ans