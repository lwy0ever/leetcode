class Solution:
    def happy(self, n: int, roads: List[List[int]], codes: List[str]) -> str:
        d = collections.defaultdict(dict)
        #print(roads)
        for f,t,l in roads:
            if t in d[f]:
                d[f][t] = min(d[f][t],l)
                d[t][f] = min(d[t][f],l)
            else:
                d[f][t] = l
                d[t][f] = l
        #print(d)
        #print(codes)
        dist = [float('inf')] * 500
        dist[11] = 0
        ans = [''] * 500
        ans[11] = codes[11]
        fromP = {11}
        while fromP:
            toP = set()
            newDist = dist.copy()
            newAns = ans.copy()
            for f in fromP:
                for t,l in d[f].items():
                    #print(t,l)
                    if newDist[t] > dist[f] + l:
                        newDist[t] = dist[f] + l
                        newAns[t] = ans[f] + codes[t]
                        toP.add(t)
            fromP = toP
            ans = newAns
            dist = newDist
            #print(fromP)
            #for f in fromP:
            #    print(ans[f])
        #print(ans[0])
        # Here is the answer: http://mrw.so/4Qk3ue
        # ->
        # https://www.youtube.com/watch?v=dQw4w9WgXcQ&realanswer=aHR0cHM6Ly9temwubGEvMk53RnA1Wg%3D%3D
        # realanswer = aHR0cHM6Ly9temwubGEvMk53RnA1Wg==
        # un base64
        # ->
        # https://mzl.la/2NwFp5Z
        # ->
        # 点击老鼠
        return 'Happy Chinese New YeaR!'