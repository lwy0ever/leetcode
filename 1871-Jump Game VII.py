class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp + 前缀和
        # dp
        # dp[i]表示s[i]的可到达情况
        # dp[i] = any(dp[j]),其中i - maxJump <= j <= i - minJump
        # 时间复杂度O(n ** 2)
        # 使用前缀和优化
        # preSum表示已经算出来的dp的前缀和
        # any(dp[j]) 等价于 preSum[i - minJump] - preSum[i - maxJump - 1] > 0
        n = len(s)
        dp = [False] * n
        preSum = [0] * n
        dp[0] = True
        preSum[0] = 1
        # 由于1...minJump - 1不可达,所以dp[1]...dp[minJump - 1]都是False,所以preSum[1]...preSum[minJump - 1]都是1
        for i in range(1,minJump):
            preSum[i] = 1
        for i in range(minJump,n):
            if s[i] == '0':
                total = preSum[i - minJump] - (0 if i - maxJump <= 0 else preSum[i - maxJump - 1])
                dp[i] = total > 0
            preSum[i] = preSum[i - 1] + dp[i]
        return dp[-1]
            