class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        fa = {}
        for rs in regions:
            for r in rs[1:]:
                fa[r] = rs[0]
        #print(fa)
        exists = set()
        r1 = region1
        r2 = region2
        while True:
            #print(r1,r2,exists)
            if r1 in exists:
                return r1
            if r2 in exists:
                return r2
            if r1 == r2:
                return r1
            if r1 != '':
                exists.add(r1)
            if r2 != '':
                exists.add(r2)
            r1 = fa.get(r1,'')
            r2 = fa.get(r2,'')