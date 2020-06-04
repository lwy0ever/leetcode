class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j]的含义是到nums1[i-1]和nums2[j-1]为止的子序列的最大点积
        # 其中dp[i][j]有四种选择
        # 1,只选择nums1[i-1]和nums2[j-1]
        # 2,选择nums1[i-1],不选择nums2[j-1]
        # 3,不选择nums1[i-1],选择nums2[j-1]
        # 4,选择nums1[i-1]和nums2[j-1],同时选择前面的
        m = len(nums1)
        n = len(nums2)
        inf = -1000 * 1000
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                dp[i][j] = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i][j],dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1] + dp[i][j])
        return dp[m][n]