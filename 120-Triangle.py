class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n    # 从下往上,dp[i]表示归集到第row行时,triangle[row][i]的最小值
        for i in range(n):
            dp[i] = triangle[-1][i]
        for row in range(n - 2,-1,-1):
            for i in range(row + 1):
                dp[i] = min(dp[i],dp[i + 1]) + triangle[row][i]
            #print(dp)
        return dp[0]