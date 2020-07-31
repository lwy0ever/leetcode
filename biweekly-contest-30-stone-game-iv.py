class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        sq = []
        i = 1
        while i * i <= n:
            sq.append(i * i)
            i += 1
        dp = [False] * (n + 1)
        i = 1
        while i <= n:
            for s in sq:
                if i >= s:
                    if dp[i - s] == False:
                        dp[i] = True
                        break
                else:
                    break
            i += 1
        #print(dp)
        return dp[-1]