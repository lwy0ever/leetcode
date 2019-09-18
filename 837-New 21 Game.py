class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # dp[x] = Alice获得x points的情况下，小于等于N的概率
        # dp[x] = (dp[x + 1] + dp[x + 2] + ... + dp[x + W]) / W

        # dp[x] = 1.0 when K <= x <= N, else 0.0
        dp = [0] * (N + W + 1)
        for i in range(K,N + 1):
            dp[i] = 1
        
        # dp[x] = (dp[x + 1] + dp[x + 2] + ... + dp[x + W]) / W
        # -->
        # dp[x + 1] - dp[x] = (dp[x + W + 1] - dp[x + 1]) / W
        # -->
        # dp[x] = (dp[x + 1] * (W + 1) - dp[x + W + 1]) / W
        dp[K - 1] = min(N - K + 1, W) / W
        for i in range(K - 2,-1,-1):
            #s = 0
            #for j in range(i + 1,i + W + 1):
            #    s += dp[j]
            s = dp[i + 1] * (W + 1) - dp[i + W + 1]
            dp[i] = s / W
            #print(dp)
        return dp[0]
