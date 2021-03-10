class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        # bfs + dp
        # bfs部分
        # 每次bfs的目标,是从某个点开始,经过任意一个O之后,到达任意一个之前没有到达过的M
        # 所以在bfs的时候,除了记录位置,还需要记录是否曾经经过O
        # 最后一次bfs,是从某个点开始,到达T
        # dp部分
        # 有num个M,需要确定光顾的先后顺序,使用dp解决
        # 先将M - O - M的最小步数记录下来
        # 用dp[mask][pos]记录
        # mask是二进制形式表示的遍历情况(num<=16),有2 ** num种情况
        # dp[mask][pos]表示已经遍历了mask为1的位置所在的M,目前在第pos个M的位置,需要的最小步数
        di = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(maze)
        n = len(maze[0])
        distMM = dict() # distMM[i][j]表示Ms[i]到Ms[j],且经过了一个O的最短距离
        distMO = dict() # 表示Ms[i]到Os[j]的最短距离
        # 计算从start开始,到达每个targets,需要的步数,记录到cache里
        def bfs(start,targets,cache):
            cnt = len(targets)
            step = 0
            counter = 0
            fromP = {(start[0],start[1])}
            visited = {(start[0],start[1])}
            while fromP and counter < cnt:
                step += 1
                toP = set()
                for fr,fc in fromP:
                    for dr,dc in di:
                        if 0 <= fr + dr < m and 0 <= fc + dc < n:
                            if maze[fr + dr][fc + dc] == '#': continue
                            if (fr + dr,fc + dc) not in visited:
                                toP.add((fr + dr,fc + dc))
                                visited.add((fr + dr,fc + dc))
                                if (fr + dr,fc + dc) in targets:
                                    cache[targets[(fr + dr,fc + dc)]] = step
                                    counter += 1
                fromP = toP
        
        Ms = dict()
        Os = dict()
        mLen = 0
        oLen = 0
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'M':
                    Ms[(i,j)] = mLen
                    mLen += 1
                elif maze[i][j] == 'O':
                    Os[(i,j)] = oLen
                    oLen += 1
                elif maze[i][j] == 'S':
                    S = (i,j)
                elif maze[i][j] == 'T':
                    T = (i,j)
        #print(Ms)
        #print(Os)
        if mLen == 0:   # 没有M,只需要从S到T
            Ts = {T:0}
            distST = [float('inf')]
            #print(S,Ts)
            bfs(S,Ts,distST)
            #print(distST)
            ans = distST[0]
        else:
            distMO = [[float('inf')] * oLen for _ in range(mLen)]
            for k,v in Ms.items():
                bfs(k,Os,distMO[v])
            #print('MO',distMO)
            distMM = [[float('inf')] * mLen for _ in range(mLen)]
            for i in range(mLen):
                for j in range(mLen):
                    if i == j:
                        continue
                    for k in range(oLen):
                        distMM[i][j] = min(distMM[i][j],distMO[i][k] + distMO[j][k])
            #print('MM',distMM)
            # 计算S到Os的距离
            distSO = [float('inf')] * oLen
            bfs(S,Os,distSO)
            #print(distSO)
            # 计算S到Ms,且经过了一个O的最短距离
            distSM = [float('inf')] * mLen
            for i in range(mLen):
                for j in range(oLen):
                    distSM[i] = min(distSM[i],distSO[j] + distMO[i][j])
            #print(distSM)
            # 计算Ms到T的距离
            distMT = [float('inf')] * mLen
            bfs(T,Ms,distMT)
            #print(distMT)
            #dp部分
            dp = [dict() for _ in range(1 << mLen)]
            for p in range(mLen):
                dp[1 << p][p] = distSM[p]
            for mask in range(1,1 << mLen):
                # 从dp[mask][p1]状态到p2点
                for p1,v in dp[mask].items():
                    for p2 in range(mLen):
                        if p1 == p2 or mask & (1 << mask):
                            continue
                        if p2 in dp[mask | (1 << p2)]:
                            dp[mask | (1 << p2)][p2] = min(dp[mask | (1 << p2)][p2],v + distMM[p1][p2])
                        else:
                            dp[mask | (1 << p2)][p2] = v + distMM[p1][p2]
            #print(dp)
            ans = float('inf')
            for p,v in dp[(1 << mLen) - 1].items():
                ans = min(ans,v + distMT[p])
        return -1 if ans == float('inf') else ans