class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [n + 1] * n # dp[i]表示在arr[:i]的范围内,子数组之和等于target的最小子数组长度
        pre = dict()    # 记录子数组的和以及其位置
        pre[0] = -1
        s = 0
        ans = n + 1
        for i,a in enumerate(arr):
            s += a
            pre[s] = i
            dp[i] = dp[i - 1]
            #print(i,a,dp)
            miniTarget = s - target
            if miniTarget in pre:   # sum(arr[pre[s - target] + 1:i + 1]) == target
                prePos = pre[miniTarget]
                if dp[prePos] < n + 1: # 在pre[s - target]之前有满足条件的子数组
                    ans = min(ans,dp[prePos] + i - prePos)
                dp[i] = min(i - prePos, dp[i - 1])
        #print(dp)
        return -1 if ans == n + 1 else ans