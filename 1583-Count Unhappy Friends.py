class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pre = dict()    # pre(a,b)表示a->b的亲近程度的排序号(base0)
        for i in range(n):
            for j in range(n - 1):
                pre[(i,preferences[i][j])] = j
        #print(pre)
        
        ans = set()
        for x,y in pairs:
            for u,v in pairs:
                if x == u and y == v:
                    continue
                if pre[(x,u)] < pre[(x,y)] and pre[(u,x)] < pre[(u,v)]:
                    ans.add(x)
                x,y = y,x
                if pre[(x,u)] < pre[(x,y)] and pre[(u,x)] < pre[(u,v)]:
                    ans.add(x)
                u,v = v,u
                if pre[(x,u)] < pre[(x,y)] and pre[(u,x)] < pre[(u,v)]:
                    ans.add(x)
                x,y = y,x
                if pre[(x,u)] < pre[(x,y)] and pre[(u,x)] < pre[(u,v)]:
                    ans.add(x)
        return len(ans)