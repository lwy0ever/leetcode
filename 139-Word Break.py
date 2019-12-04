class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dic = set(wordDict)
        dp = [0] * (n + 1) #dp[i]表示s[:i]是否可以被字典组成
        dp[0] = 1
        for i in range(1,n + 1):
            for j in range(1,i + 1):
                #print(i,j,dp[j - 1],s[j - 1:i])
                if dp[j - 1] and (s[j - 1:i] in dic):
                    dp[i] = 1
                    break
        #print(dp)
        return dp[-1]