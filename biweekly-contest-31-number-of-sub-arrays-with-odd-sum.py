class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 内存优化
        # 子数组要求是连续数组
        n = len(arr)
        ans = 0
        even = 0    # even表示选择arr[i]的偶数和子数组个数
        odd = 0     # odd表示选择arr[i]的奇数和子数组个数
        for i in range(n):
            if arr[i] & 1:
                even,odd = odd,even + 1 # 偶数和子数组+arr[i] or arr[i]自身
            else:
                even = even + 1 # 偶数和子数组+arr[i] or arr[i]自身
                #odd = odd
            ans += odd
        #print(dp[0])
        #print(dp[1])
        return ans % (10 ** 9 + 7)

        '''
        # 子数组要求是连续数组
        n = len(arr)
        ans = 0
        # dp[0][i + 1]表示选择arr[i]的偶数和子数组个数
        # dp[1][i + 1]表示选择arr[i]的奇数和子数组个数
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(n):
            if arr[i] & 1:
                dp[0][i + 1] = dp[1][i]
                dp[1][i + 1] = dp[0][i] + 1 # 偶数和子数组+arr[i] or arr[i]自身
            else:
                dp[0][i + 1] = dp[0][i] + 1 # 偶数和子数组+arr[i] or arr[i]自身
                dp[1][i + 1] = dp[1][i]
            ans += dp[1][i + 1]
        #print(dp[0])
        #print(dp[1])
        return ans % (10 ** 9 + 7)
        '''