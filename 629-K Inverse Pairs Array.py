class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # 将1...n,逐步放入数组
        # 放入1,逆序对0个
        # 放入2,逆序对可以是0,1
        # 放入3,逆序对可以是0 + 0,0 + 1,0 + 2,1 + 0,1 + 1,1 + 2
        # 也就是说,放入数字i的时候,可以增加0到i - 1个逆序对
        # dp[i]表示当前逆序对为i个的可能数组个数
        # 转移方程查看官方题解
        mod = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for num in range(1,n + 1):    # 放入第num个数字
            newDP = [0] * (k + 1)
            for i in range(k + 1):
                newDP[i] = (newDP[i - 1] if i - 1 >= 0 else 0) - (dp[i - num] if i - num >= 0 else 0) + dp[i]
                newDP[i] %= mod
            dp = newDP
        return dp[-1]