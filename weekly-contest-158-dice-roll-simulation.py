class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # 搞一个二维数组dp[i][j]
        # 表示到目前位置,筛子i连续出现j + 1次的方案数
        six = 6
        m = 10 ** 9 + 7
        dp = list()
        for r in rollMax:
            dp.append([0] * r)
        #print(dp)
        for d in dp:
            d[0] = 1
        s = sum([sum(d) for d in dp])
        #print(dp)
        for _ in range(n - 1):
            newDP = list()
            for r in rollMax:
                newDP.append([0] * r)
            for i in range(six):
                newDP[i][0] = s - sum(dp[i][0:])
                newDP[i][1:] = dp[i][:-1]                
            dp = newDP
            s = sum([sum(d) for d in dp]) % m
            #print(dp)
        return s
