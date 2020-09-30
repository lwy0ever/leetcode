class Solution:
    def numPermsDISequence(self, S: str) -> int:
        # dp + 内存优化
        # 我们不关心具体选择的数字x,只关心剩余的数字有多少小于x,多少大于x
        n = len(S)
        # 共有n + 1个数字需要选择
        # dp[i][j]表示已经选择了i + 1个数字,还有n + 1 - (i + 1)个数字可以选择,其中有j个数字小于x的情况下的排列数量
        # 转移方程:
        # 如果是D
        # dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j + 2] + ... + dp[i - 1][left + 1] = sum(dp[i - 1][j + 1:left + 2])
        # 如果是I
        # dp[i][j] = dp[i - 1][0] + dp[i - 1][1] + ... + dp[i - 1][j] = sum(dp[i - 1][:j + 1])
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = 1
        for i in range(1,n + 1):
            left = n - i    # 还有n + 1 - (i + 1)个数字可以选择
            if S[i - 1] == 'D':
                for j in range(left + 1):
                    dp[j] = sum(dp[j + 1:left + 2])
            else:
                for j in range(left,-1,-1):
                    dp[j] = sum(dp[:j + 1])
        #print(dp)
        return dp[0] % (10 ** 9 + 7)

        '''
        # dp
        # 我们不关心具体选择的数字x,只关心剩余的数字有多少小于x,多少大于x
        n = len(S)
        # 共有n + 1个数字需要选择
        # dp[i][j]表示已经选择了i + 1个数字,还有n + 1 - (i + 1)个数字可以选择,其中有j个数字小于x的情况下的排列数量
        # 转移方程:
        # 如果是D
        # dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j + 2] + ... + dp[i - 1][left + 1] = sum(dp[i - 1][j + 1:left + 2])
        # 如果是I
        # dp[i][j] = dp[i - 1][0] + dp[i - 1][1] + ... + dp[i - 1][j] = sum(dp[i - 1][:j + 1])
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(1,n + 1):
            left = n - i    # 还有n + 1 - (i + 1)个数字可以选择
            for j in range(left + 1):
                if S[i - 1] == 'D':
                    dp[i][j] = sum(dp[i - 1][j + 1:left + 2])
                else:
                    dp[i][j] = sum(dp[i - 1][:j + 1])
        #print(dp)
        return dp[n][0] % (10 ** 9 + 7)
        '''