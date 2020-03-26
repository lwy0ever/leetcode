class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        d = collections.defaultdict(dict)
        for i in range(n):
            d[equations[i][0]][equations[i][1]] = values[i]
            d[equations[i][1]][equations[i][0]] = 1 / values[i]
        ans = []
        for q in queries:
            if q[0] not in d or q[1] not in d:
                ans.append(-1)
                continue
            # bfs
            fromP = {q[0]:1}
            visited = {q[0]}
            while fromP:
                if q[1] in fromP:
                    ans.append(fromP[q[1]])
                    break
                toP = {}
                for f,fv in fromP.items():
                    for t,tv in d[f].items():
                        if t not in visited:
                            toP[t] = fv * tv
                            visited.add(t)
                fromP = toP
            # 如果是由于找不到q[1]而退出的,添加-1
            if not fromP:
                ans.append(-1)
        return ans