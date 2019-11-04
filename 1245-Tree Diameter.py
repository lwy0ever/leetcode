class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        self.ans = 0
        
        def find(fromP,cur):
            #print('find',fromP,cur)
            if len(d[cur]) == 1 and d[cur][0] == fromP:
                return 0
            l = []
            for t in d[cur]:
                if t == fromP:
                    continue
                l.append(find(cur,t))
            #print(l)
            if len(l) > 1:
                l.sort()
                self.ans = max(self.ans,l[-1] + l[-2] + 2)
            return l[-1] + 1
        
        t = find(-1,0)
        self.ans = max(self.ans,t)
        return self.ans