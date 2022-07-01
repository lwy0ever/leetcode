class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        # 不考虑删除,考虑保留
        # 定义dp[i]为,保留第i位的情况下,前0...i列可以保留的列数
        # 如果所有行的第j列都<=第i列,则dp[i] = max(dp[i],dp[j] + 1)
        dp = [1] * m
        for i in range(1,m):
            for j in range(i):
                if all(strs[x][j] <= strs[x][i] for x in range(n)):
                    dp[i] = max(dp[i],dp[j] + 1)
            #print(i,dp)
        return m - max(dp)