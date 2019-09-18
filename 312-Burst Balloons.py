class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 解题思路：如何使最终结果最大化？动态规划保存结果
        # 1.将问题拆解成求i->j的最大值，最大的i=0,j=n
        # 2.从i->j中找一个k，拆分求解，i->k,k,k->j三个值之和的最大值
        # 3.i->k和k->j代表k的左边和右边全部戳破求解的最大值
        # 4.左右全部戳破后，k的值为num[i]*num[k]*num[j]
        # 5.动态转移方程：dp[i][j]=Math.max(dp[i][j],dp[i][k]+dp[k][j]+num[i]*num[k]*num[j])
        
        # dp[i][j]表示戳破i + 1到j - 1的最大值,不戳i和j
        # 所以i最大值为n - 3,j最大值为n - 1
        nums.insert(0,1)
        nums.append(1)
        #rint(nums)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # 需要ij的差从2开始,到n + 1
        for ij in range(2,n + 1):   # i和j的差
            for i in range(n - ij):
                j = i + ij
                for k in range(i + 1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][n - 1]
        
