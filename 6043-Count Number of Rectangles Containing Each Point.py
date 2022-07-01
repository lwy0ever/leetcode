class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 注意到hi,yj <= 100
        xs = dict()
        ns = dict()
        for l,h in rectangles:
            if h not in xs:
                xs[h] = []
                ns[h] = 0
            xs[h].append(l)
            ns[h] += 1
        for i in xs.keys():
            xs[i].sort()
        heights = sorted(xs.keys(),reverse = True)
        #print(xs)
        n = len(points)
        ans = [0] * n
        for i,(x,y) in enumerate(points):
            #print(i,x,y)
            for h in heights:
                if y > h:
                    break
                p = bisect.bisect_left(xs[h],x)
                #print(xs[h],x,p)
                ans[i] += ns[h] - p
                #print(h,ans[i])
        return ans