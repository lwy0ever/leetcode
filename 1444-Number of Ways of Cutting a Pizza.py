class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # 每切一刀,剩余部分一定是一个长方形(含正方形)
        # 从右下角开始
        rows = len(pizza)
        cols = len(pizza[0])
        M = 10 ** 9 + 7
        # pre[i][j]表示从pizza[i][j]到右下角的苹果数量
        pre = [[0] * cols for _ in range(rows)]
        for i in range(rows - 1,-1,-1):
            for j in range(cols - 1,-1,-1):
                apple = pizza[i][j] == 'A'
                if j == cols - 1:
                    if i == rows - 1:
                        pre[i][j] = apple
                    else:
                        pre[i][j] = pre[i + 1][j] + apple
                else:
                    if i == rows - 1:
                        pre[i][j] = pre[i][j + 1] + apple
                    else:
                        pre[i][j] = pre[i][j + 1] + pre[i + 1][j] - pre[i + 1][j + 1] + apple
        #print(pre)
        # dp[t][i][j]表示以pizza[i][j]为左上角的长方形,可以分给t + 1个人的方案数
        dp = [[[0] * cols for _ in range(rows)] for _ in range(k)]
        for i in range(rows - 1,-1,-1):
            for j in range(cols - 1,-1,-1):
                if pre[i][j]:
                    dp[0][i][j] = 1
        #print(dp[0])
        for t in range(1,k):
            for i in range(rows - 1,-1,-1):
                for j in range(cols - 1,-1,-1):
                    for x in range(i + 1,rows): # 横切
                        if pre[i][j] - pre[x][j]:
                            dp[t][i][j] += dp[t - 1][x][j]
                    for y in range(j + 1,cols): # 竖切
                        if pre[i][j] - pre[i][y]:
                            dp[t][i][j] += dp[t - 1][i][y]
        #print(dp)
        return dp[k - 1][0][0] % M