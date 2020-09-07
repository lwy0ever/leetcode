class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 1,如果岛本身就是分离的,返回0
        # 2,如果岛需要1天分离,返回1
        # 3,如果1天无法分离,那么2天一定可以分离
        # 3.x,说明:一定存在一个角,和2个点有连接
        #     0 1 1 1
        #     0 1 1 1
        #     0 1 1 0
        # 例如左下角这个点,所以可以通过改变其上+右的位置,使其分离
        m = len(grid)
        n = len(grid[0])
        ones = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.add((i,j))
        if len(ones) == 0:
            return 0
        di = [[-1,0],[1,0],[0,-1],[0,1]]
        # 任选一个1,bfs
        one = ones.pop()
        ones.add(one)
        
        def bfs(one):
            fromP = {one}
            visited = {one}
            while fromP:
                toP = set()
                for fr,fc in fromP:
                    for dr,dc in di:
                        r = fr + dr
                        c = fc + dc
                        if 0 <= r < m and 0 <= c < n:
                            if (r,c) not in visited and grid[r][c] == 1:
                                visited.add((r,c))
                                toP.add((r,c))
                fromP = toP
            return len(visited)

        # 没有遍历所有的1,说明本身就是分离的
        if bfs(one) < len(ones):
            return 0
        
        # 尝试将1变为0
        for fr,fc in ones:
            cnt = 0
            for dr,dc in di:
                r = fr + dr
                c = fc + dc
                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1:
                        cnt += 1
            # 只有1的连接点的点,改变无意义
            if cnt == 1:
                continue
            # 尝试改变(fr,fc)
            grid[fr][fc] = 0
            for dr,dc in di:
                r = fr + dr
                c = fc + dc
                if 0 <= r < m and 0 <= c < n:
                    # 找一个相邻的1,开始bfs
                    if grid[r][c] == 1:
                        break
            # bfs结果不是所有的1
            if bfs((r,c)) < len(ones) - 1:
                return 1
            grid[fr][fc] = 1
        return 2
        