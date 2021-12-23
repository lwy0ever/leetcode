class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 本质上,是把石子分成2堆,相互消耗
        # dp[i]表示总重量为i的一堆是否存在
        total = sum(stones)
        half = total // 2   # 最多一堆重量为half
        dp = [False] * (half + 1)
        dp[0] = True
        for s in stones:
            for i in range(half,s - 1,-1):  # 注意,必须倒序
                if dp[i - s]:
                    dp[i] |= dp[i - s]
        #print(dp)
        for i in range(half,-1,-1):
            if dp[i]:
                return total - i * 2