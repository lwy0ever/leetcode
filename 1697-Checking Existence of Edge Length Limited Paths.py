class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 并查集
        # 只关心是否连通,不关心如何连通,所以可以用并查集
        # 将edgeList按照dis排序,先把dis小的并进去
        # 将queries按照limit排序,先检查limit小的
        # 如果query中的p,q连通(由于limit <= dis),则true,否则false
        edgeList.sort(key = lambda x:x[2])
        
        qn = len(queries)
        qIndexS = list(range(qn))
        qIndexS.sort(key = lambda x:queries[x][2])
        
        ans = [False] * qn
        en = len(edgeList)

        # 并查集
        def getFather(x):
            # 注意这里,不用while,用if就可以
            # 但是需要father[x] = getFather(father[x])
            # 同时return father[x]
            if father[x] != x:
                father[x] = getFather(father[x])
            return father[x]
                
        father = [i for i in range(n)]  # 初始化并查集
        ei = 0
        for qIndex in qIndexS:
            p,q,limit = queries[qIndex]
            while ei < en and edgeList[ei][2] < limit:
                u,v,_ = edgeList[ei]
                uf = getFather(u)
                vf = getFather(v)
                if uf != vf:
                    father[vf] = uf
                ei += 1
            if getFather(p) == getFather(q):
                ans[qIndex] = True
            #print(qIndex,p,q,limit,u,v,uf,vf,father,ans)
        return ans