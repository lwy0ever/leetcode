class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]  # dp[i][j]为1,表示s1[:i]和s2[:j]可以交错组成s3[:i + j],dp[i][j]为0表示不能组成
        dp[0][0] = 1
        for i in range(1,n1 + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0]:
                dp[i][0] = 1
        for i in range(1,n2 + 1):
            if s2[i - 1] == s3[i - 1] and dp[0][i - 1]:
                dp[0][i] = 1

        for i in range(1,n1 + 1):
            for j in range(1,n2 + 1):
                if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = 1

        #print(dp)
        return dp[-1][-1]