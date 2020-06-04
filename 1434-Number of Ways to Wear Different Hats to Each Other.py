class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        n = len(hats)   # 人数n
        target = (1 << n) - 1
        dp = [[0] * (1 << n) for _ in range(41)]   # dp[i][j]表示考虑前i个帽子的情况下,状态为j的方案数
        # 0 <= j <= (1 << n) - 1,二进制的形式表示戴帽子的情况
        hatPerson = [[] for _ in range(41)] # 帽子-人的关系
        for i in range(n):
            for h in hats[i]:
                hatPerson[h].append(i)
        dp[0][0] = 1
        for i in range(1,41):
            for j in range(1 << n):
                dp[i][j] = dp[i - 1][j]
                for p in hatPerson[i]:
                    mask = 1 << p   # 编号为p的人,戴帽子的状态为mask
                    if mask & j == 0:   # 状态j的情况下,p不戴帽子,所以不用考虑
                        continue
                    dp[i][j] += dp[i - 1][j - mask]  # 从p不戴帽子变成p戴帽子
                dp[i][j] %= M
        return dp[-1][-1]