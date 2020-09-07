class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        #'''
        # dp,改成递归剪枝,内存优化,但是速度变慢了一些
        n = len(stoneValue)
        s = [[0] * (n - i) for i in range(n)] # s[i][l]表示sum(stoneValue[i:i + l + 1])
        for i in range(n):
            s[i][0] = stoneValue[i]
            for l in range(1,n - i):
                s[i][l] = s[i][l - 1] + stoneValue[i + l]
        #print(s)
        dp = [[0] * (n - i) for i in range(n)]    # dp[i][l]表示stoneValue[i:i + l + 2]的结果,l + 1是stoneValue[i:i + l + 2]的长度

        def dfs(start,end):
            l = end - start
            if dp[start][l] > 0:
                return dp[start][l]
            _max = 0
            for m in range(start,end):
                #print(start,m,end)
                lenLeft = m - start
                lenRight = end - m - 1
                if s[start][lenLeft] > s[m + 1][lenRight]:
                    _max = max(_max,dfs(m + 1,end) + s[m + 1][lenRight])
                elif s[start][lenLeft] < s[m + 1][lenRight]:
                    _max = max(_max,dfs(start,m) + s[start][lenLeft])
                else:   # s[start][lenLeft] == s[m + 1][lenRight]
                    _max = max(_max,dfs(start,m) + s[start][lenLeft],dfs(m + 1,end) + s[m + 1][lenRight])
            dp[start][l] = _max
            return dp[start][l]
        dfs(0,n - 1)
        return dp[0][n - 1]
        '''
        # dp,改成递归剪枝
        n = len(stoneValue)
        s = [[0] * n for _ in range(n)] # s[i][j]表示sum(stoneValue[i:j + 1])
        for i in range(n):
            s[i][i] = stoneValue[i]
            for j in range(i + 1,n):
                s[i][j] = s[i][j - 1] + stoneValue[j]
        #print(s)
        dp = [[0] * n for _ in range(n)]    # dp[i][j]表示stoneValue[i:j + 1]的结果

        def dfs(start,end):
            if dp[start][end] > 0:
                return dp[start][end]
            _max = 0
            for m in range(start,end):
                if s[start][m] > s[m + 1][end]:
                    _max = max(_max,dfs(m + 1,end) + s[m + 1][end])
                elif s[start][m] < s[m + 1][end]:
                    _max = max(_max,dfs(start,m) + s[start][m])
                else:   # s[start][m] == s[m + 1][end]
                    _max = max(_max,dfs(start,m) + s[start][m],dfs(m + 1,end) + s[m + 1][end])
            dp[start][end] = _max
            return dp[start][end]
        dfs(0,n - 1)
        return dp[0][n - 1]
        '''
        '''
        # dp,递归
        cache = dict()
        n = len(stoneValue)

        def getMax(start,end):
            if end - start == 1:    # 递归出口, 只有1个石头, 返回0
                return 0
            if (start,end) not in cache:
                # 先计算当前的总和
                s = sum(stoneValue[start:end])
                # 记录左侧行的当前和
                leftsum = 0
                _max = 0
                for i in range(start,end):
                    leftsum += stoneValue[i]
                    rightsum = s - leftsum
                    # 模拟题目的三种情况,进行切片
                    # !!!这里同时实现了剪枝
                    if leftsum < rightsum:
                        _max = max(_max, leftsum + getMax(start,i + 1))
                    elif leftsum == rightsum:
                        _max = max(_max, leftsum + getMax(start,i + 1),rightsum + getMax(i + 1,end))
                    else:   # leftsum > rightsum
                        _max = max(_max, rightsum + getMax(i + 1,end))
                cache[(start,end)] = _max
            return cache[(start,end)]

        return getMax(0,n)
        '''
        '''
        # dp,无法剪枝,会超时
        n = len(stoneValue)
        s = [[0] * n for _ in range(n)] # s[i][j]表示sum(stoneValue[i:j + 1])
        for i in range(n):
            s[i][i] = stoneValue[i]
            for j in range(i + 1,n):
                s[i][j] = s[i][j - 1] + stoneValue[j]
        #print(s)
        c = set()
        dp = [[0] * n for _ in range(n)]    # dp[i][j]表示stoneValue[i:j + 1]的结果
        for length in range(1,n):
            for i in range(n - length):
                j = i + length
                _max = 0
                for m in range(i,j):
                    m2 = m + 1
                    if s[i][m] > s[m2][j]:
                        _max = max(_max,dp[m2][j] + s[m2][j])
                    elif s[i][m] < s[m2][j]:
                        _max = max(_max,dp[i][m] + s[i][m])
                    else:   # s[i][m] == s[m2][j]
                        _max = max(_max,dp[i][m] + s[i][m],dp[m2][j] + s[m2][j])
                    #print(i,m,j,s[i][m],s[m + 1][j],stoneValue[i:j + 1],dp[i][j])
                dp[i][j] = _max
        #print(dp)
        return dp[0][n - 1]
        '''