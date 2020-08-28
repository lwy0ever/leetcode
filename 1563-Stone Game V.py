class Solution:\u000A    def stoneGameV(self, stoneValue: List[int]) \u002D\u003E int:\u000A        # dp,改成递归剪枝\u000A        n \u003D len(stoneValue)\u000A        s \u003D [[0] * n for _ in range(n)] # s[i][j]表示sum(stoneValue[i:j + 1])\u000A        for i in range(n):\u000A            s[i][i] \u003D stoneValue[i]\u000A            for j in range(i + 1,n):\u000A                s[i][j] \u003D s[i][j \u002D 1] + stoneValue[j]\u000A        #print(s)\u000A        c \u003D set()\u000A        dp \u003D [[0] * n for _ in range(n)]    # dp[i][j]表示stoneValue[i:j + 1]的结果\u000A\u000A        def dfs(start,end):\u000A            if dp[start][end] \u003E 0:\u000A                return dp[start][end]\u000A            _max \u003D 0\u000A            for m in range(start,end):\u000A                if s[start][m] \u003E s[m + 1][end]:\u000A                    _max \u003D max(_max,dfs(m + 1,end) + s[m + 1][end])\u000A                elif s[start][m] \u003C s[m + 1][end]:\u000A                    _max \u003D max(_max,dfs(start,m) + s[start][m])\u000A                else:   # s[start][m] \u003D\u003D s[m + 1][end]\u000A                    _max \u003D max(_max,dfs(start,m) + s[start][m],dfs(m + 1,end) + s[m + 1][end])\u000A            dp[start][end] \u003D _max\u000A            return dp[start][end]\u000A        dfs(0,n \u002D 1)\u000A        return dp[0][n \u002D 1]\u000A        \u0027\u0027\u0027\u000A        # dp,递归\u000A        cache \u003D dict()\u000A        n \u003D len(stoneValue)\u000A\u000A        def getMax(start,end):\u000A            if end \u002D start \u003D\u003D 1:    # 递归出口, 只有1个石头, 返回0\u000A                return 0\u000A            if (start,end) not in cache:\u000A                # 先计算当前的总和\u000A                s \u003D sum(stoneValue[start:end])\u000A                # 记录左侧行的当前和\u000A                leftsum \u003D 0\u000A                _max \u003D 0\u000A                for i in range(start,end):\u000A                    leftsum +\u003D stoneValue[i]\u000A                    rightsum \u003D s \u002D leftsum\u000A                    # 模拟题目的三种情况,进行切片\u000A                    # !!!这里同时实现了剪枝\u000A                    if leftsum \u003C rightsum:\u000A                        _max \u003D max(_max, leftsum + getMax(start,i + 1))\u000A                    elif leftsum \u003D\u003D rightsum:\u000A                        _max \u003D max(_max, leftsum + getMax(start,i + 1),rightsum + getMax(i + 1,end))\u000A                    else:   # leftsum \u003E rightsum\u000A                        _max \u003D max(_max, rightsum + getMax(i + 1,end))\u000A                cache[(start,end)] \u003D _max\u000A            return cache[(start,end)]\u000A\u000A        return getMax(0,n)\u000A        \u0027\u0027\u0027\u000A        \u0027\u0027\u0027\u000A        # dp,无法剪枝,会超时\u000A        n \u003D len(stoneValue)\u000A        s \u003D [[0] * n for _ in range(n)] # s[i][j]表示sum(stoneValue[i:j + 1])\u000A        for i in range(n):\u000A            s[i][i] \u003D stoneValue[i]\u000A            for j in range(i + 1,n):\u000A                s[i][j] \u003D s[i][j \u002D 1] + stoneValue[j]\u000A        #print(s)\u000A        c \u003D set()\u000A        dp \u003D [[0] * n for _ in range(n)]    # dp[i][j]表示stoneValue[i:j + 1]的结果\u000A        for length in range(1,n):\u000A            for i in range(n \u002D length):\u000A                j \u003D i + length\u000A                _max \u003D 0\u000A                for m in range(i,j):\u000A                    m2 \u003D m + 1\u000A                    if s[i][m] \u003E s[m2][j]:\u000A                        _max \u003D max(_max,dp[m2][j] + s[m2][j])\u000A                    elif s[i][m] \u003C s[m2][j]:\u000A                        _max \u003D max(_max,dp[i][m] + s[i][m])\u000A                    else:   # s[i][m] \u003D\u003D s[m2][j]\u000A                        _max \u003D max(_max,dp[i][m] + s[i][m],dp[m2][j] + s[m2][j])\u000A                    #print(i,m,j,s[i][m],s[m + 1][j],stoneValue[i:j + 1],dp[i][j])\u000A                dp[i][j] \u003D _max\u000A        #print(dp)\u000A        return dp[0][n \u002D 1]\u000A        \u0027\u0027\u0027