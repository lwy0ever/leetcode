class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 方法1:数学
        # 因为是偶数堆,分成 奇数堆 和 偶数堆.初始情况,两端是不同的奇偶堆
        # 哪堆大,则Alexa先取哪堆
        # 如果Alexa取了奇数堆的一堆,那么Lee只能选择偶数堆,然后Alexa继续选择奇数堆
        # 反之亦然
        # so,Alexa必胜
        return True
        
        # 方法2:dp
        n = len(piles)
        # dp[i]表示piles[i:i + length]范围,先取的一方比后取的一方多获得的石子数量
        dp = [0] * n
        for i in range(n):
            dp[i] = piles[i]
        for l in range(2,n + 1):
            newDP = []
            for i in range(n - l + 1):
                newDP.append(max(piles[i] - dp[i + 1],piles[i + l - 1] - dp[i]))
            dp = newDP
            #print(dp)
        return dp[0] > 0