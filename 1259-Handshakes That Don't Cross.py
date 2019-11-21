class Solution:
    def numberOfWays(self, num_people: int) -> int:
        n = num_people
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(2,n + 1):
            if i % 2 == 0:
                for j in range(0,i - 1,2):
                    #print(i,j,i - 2 - j)
                    dp[i] += dp[j] * dp[i - 2 - j]
        #print(dp)
        return dp[-1] % (10 ** 9 + 7)