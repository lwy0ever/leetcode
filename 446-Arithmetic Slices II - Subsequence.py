class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        # dp[i][d]表示以A[i]为结尾元素,等差值为d的序列的个数(序列最少2个元素)
        ans = 0
        for last in range(1,n):
            for preLast in range(last):
                d = A[preLast] - A[last]    # 序列preLast,last
                dp[last][d] += dp[preLast][d] + 1   # dp[preLast][d]的每个起点都可以作为dp[last][d]的起点,增加了一个起点:preLast
                ans += dp[preLast][d]   # 由于A[last]作为第n(n >= 3)个元素了,所以加上A[last]以后,dp[preLast][d]的序列都够3个元素了
                #print(preLast,last,dp)
        return ans