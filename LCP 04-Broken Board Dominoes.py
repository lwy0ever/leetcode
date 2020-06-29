class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        b = set()
        for i,j in broken:
            b.add((i,j))
        # 使用动态规划的思路
        # 考虑每一个点是否可以放置骨牌:
        # 可以横放,表示放置在该点和该点左侧的点
        # 可以竖放,表示放置在该点和该点上方的点
        # 因为是动态规划,所以考虑该点及该点之前点的状态
        # dp
        # dp[x]中的x表示在考虑点(i,j)的时候,点(i - 1,j),(i - 1,j + 1)...(i - 1,m - 1)...(i,0),(i,1)...(i,j - 1)这些点的可能状态,共m个点,因此有1 << m种状态
        # 用二进制压缩状态表示,1表示该点不能放置;0表示该点可以放置
        # 点(i - 1,j)的状态在二级制的最低位,这样可以通过>>操作去掉该位
        # 如果将其放在最高位,<<操作有溢出问题
        # 而dp[x]表示在这种状态下可以放置的骨牌数量
        # dp[x] == -1表示该状态不存在(例如:出界情况)
        dp = [-1] * (1 << m)
        dp[(1 << m) - 1] = 0
        for i in range(n):
            for j in range(m):
                #print(i,j)
                next_dp = [-1] * (1 << m)
                high = 1 << (m - 1) # 最高位
                if (i,j) in b:  # 坏点,不能放置
                    for status in range(1 << m):
                        next_dp[(status >> 1) | high] = max(next_dp[(status >> 1) | high],dp[status])
                    dp = next_dp
                    continue
                for status in range(1 << m):
                    ms = status >> 1
                    if status & 1 == 0 and dp[status] != -1:    # 可以竖放
                        #print('|',str(bin(status))[2:],str(bin((status >> 1) | high))[2:])
                        next_dp[ms | high] = max(next_dp[ms | high],dp[status] + 1) # 竖放
                    if j != 0:  # 非第1列,尝试横放
                        if status & high == 0 and dp[status] != -1: # 可以横放
                            nearHigh = high >> 1
                            #print('-',str(bin(status))[2:],dp[status],str(bin((status >> 1) | high | nearHigh))[2:])
                            next_dp[ms | high | nearHigh] = max(next_dp[ms | high | nearHigh],dp[status] + 1) # 横放
                    next_dp[ms] = max(next_dp[ms],dp[status]) # 不放
                dp = next_dp
                #print('\t'.join([str(bin(i))[2:].zfill(m) for i in range(1 << m)]))
                #print('\t'.join([str(dp[i]).rjust(m) for i in range(1 << m)]))
        return max(dp)
                    
            
        