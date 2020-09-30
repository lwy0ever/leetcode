class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dis(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def findGroup(i):
            while group[i] != i:
                i = group[i]
            return i
        
        dist = []
        n = len(points)
        if n <= 1:
            return 0
        for i in range(n - 1):
            for j in range(i + 1,n):
                dist.append((dis(points[i],points[j]),i,j))
        dist.sort(key = lambda x:x[0])
        #print(dist)
        group = [i for i in range(n)]   # group[i]记录points[i]所归属到的组,如果group[i]==i,说明找到了组编号
        ans = 0
        ansCounter = 1  # 需要n - 1次连接
        for d,i,j in dist:
            iG = findGroup(i)
            jG = findGroup(j)
            #print(d,i,j,iG,jG)
            if iG != jG:    # 需要连接
                #print(d,i,j)
                ans += d
                ansCounter += 1
                group[jG] = iG  # 合并两个点所在的组
                #print(group)
                if ansCounter == n:
                    return ans