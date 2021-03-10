class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n + 1)]   # dp[i][j] 表示i个硬币出现j个正面的可能性
        #print(dp)
        dp[0][0] = 1
        for i in range(1,n + 1):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
        #print(dp)
        for i in range(1,n + 1):
            for j in range(1,target + 1):
                #print(i,j)
                dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])
        #print(dp)
        return dp[-1][-1]