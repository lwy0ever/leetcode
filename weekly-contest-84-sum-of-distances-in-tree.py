class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        m = {i:[] for i in range(N)}
        for a,b in edges:
            m[a].append(b)
            m[b].append(a)

        step = 0
        child = [0] * N
        #child[0] = N - 1
        steps = [0] * N
        vd = {0}
        
        def countChild(cur,step,steps,child,vd,m):
            for p in m[cur]:
                if p in vd:
                    continue
                vd.add(p)
                child[cur] += countChild(p,step + 1,steps,child,vd,m) + 1
                steps[0] += step
            return child[cur]
        child[0] = countChild(0,1,steps,child,vd,m)
        #print(child)
        #print(steps)
        cur = [0]
        vd = {0}
        while cur:
            newCur = []
            for c in cur:
                for p in m[c]:
                    if p in vd:
                        continue
                    # 点B的距离和 = 点A的距离和 - 点B方向上的路径数 + 其他方向上的路径数
                    steps[p] = steps[c] - child[p] + (N - child[p] - 2)
                    newCur.append(p)
                    vd.add(p)
            cur = newCur
        #print(steps)
        return steps
        '''
        v = {i:{i:0} for i in range(N)}
        cur = [0]
        vd = {0}
        while cur:
            newCur = []
            for c in cur:
                for p in m[c]:
                    if p in vd:
                        continue
                    for t in vd:
                        #print(v)
                        #print(p,t,c)
                        v[p][t] = v[t][c] + 1
                        v[t][p] = v[c][t] + 1
                    vd.add(p)
                    newCur.append(p)
            cur = newCur
        #print(visited)
        ans = []
        for i in range(N):
            a = 0
            for x in v[i].values():
                a += x
            ans.append(a)
        return ans
        '''