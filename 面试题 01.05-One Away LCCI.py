class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # method 1:
        m,n = len(first),len(second)
        if m < n:
            return self.oneEditAway(second,first)
        if m - n > 1:
            return False
        for i,(a,b) in enumerate(zip(first,second)):
            if a != b:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True

        # method 2:
        # dp
        n1 = len(first)
        n2 = len(second)
        # dp[i][j]表示使first[:i + 1]和second[:j + 1]一致,需要操作的次数
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for x in range(1,n1 + 1):
            dp[x][0] = x
        for x in range(1,n2 + 1):
            dp[0][x] = x
        for i in range(1,n1 + 1):
            for j in range(1,n2 + 1):
                if first[i - 1] == second[j - 1]:
                    todo = 0
                else:
                    todo = 1
                dp[i][j] = min(dp[i - 1][j - 1] + todo,dp[i][j - 1] + 1,dp[i - 1][j] + 1)
        return dp[-1][-1] <= 1