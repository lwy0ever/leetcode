class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        d = {}
        for w in words:
            if len(set(w)) <= 7:
                d[frozenset(w)] = d.get(frozenset(w),0) + 1
        ans = []
        for p in puzzles:
            p1 = (p[0],)
            pRest = set(p[1:])
            cnt = 0
            for i in range(len(pRest) + 1):
                for c in itertools.combinations(pRest,i):
                    cnt += d.get(frozenset(c + p1),0)
            ans.append(cnt)
        return ans
        '''
        ws = [set(w) for w in words]
        ans = []
        for p in puzzles:
            n = 0
            for w in ws:
                #print(w,p)
                #print( p[1] in w)
                #print(w.issubset(p))
                if p[0] in w and w.issubset(p):
                    n += 1
            ans.append(n)
        return ans
        '''