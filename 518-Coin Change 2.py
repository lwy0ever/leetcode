class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp
        # dp[i]表示凑成i的方案数量
        # 为了避免出现1 + 2和2 + 1被统计为2种方案,将coins的循环放在外层
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(amount - c + 1):
                dp[i + c] += dp[i]
        #print(dp)
        return dp[amount]