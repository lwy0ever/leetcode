class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        # bfs
        rotten = set()
        #visited = set()
        fresh = set()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i,j))
                    #visited.add((i,j))
        timer = 0
        while rotten and fresh:
            toRotten = set()
            for rx,ry in rotten:
                for dx,dy in di:
                    if (rx + dx,ry + dy) in fresh:
                            toRotten.add((rx + dx,ry + dy))
                            #visited.add((rx + dx,ry + dy))
                            fresh.remove((rx + dx,ry + dy))
            rotten = toRotten
            timer += 1
        return -1 if fresh else timer