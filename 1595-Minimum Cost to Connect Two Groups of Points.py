class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # 所有的点都需要连接,因此连接的顺序无关
        # 逐个连接size1,状态压缩size2
        # 或者
        # 逐个连接size2,状态压缩size1
        # 由于size1 >= size2,状态压缩size2更快一些
        m = len(cost)
        n = len(cost[0])
        cache = dict()
        # 尝试size1的第ind个点(之前的点已经连接),size2的状态是status
        # 返回最低成本
        def connect(ind,status):
            if (ind,status) in cache:
                return cache[(ind,status)]
            if ind == m:    # size1都已经连接,检查size2是否有未连接的点
                ans = 0
                for i in range(n):
                    if status & (1 << i) == 0:  # size2的点i未连接
                        ans += min(cost[j][i] for j in range(m))
            else:
                ans = float('inf')
                for i in range(n):
                    ans = min(ans,cost[ind][i] + connect(ind + 1,status | (1 << i)))
            cache[(ind,status)] = ans
            return ans
        
        return connect(0,0)