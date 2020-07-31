class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * (n + 1)    # dp[i]表示i个元素可以组成的bst的数量
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n + 1):
            for j in range(1,i + 1):  # root的位置,base 1
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]