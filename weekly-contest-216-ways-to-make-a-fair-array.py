class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 没看懂的算法
        # 去除索引为i的元素后,i之前元素的奇偶性不变,i之后元素的奇偶性改变,即i之后奇/偶数下标元素的和变成了偶/奇数下标
        # 考虑奇偶元素的差值,我们求正负交替的前缀和dp[i]
        # 那么dp[i-1]表示索引i左边部分奇偶元素差值,dp[n] - dp[i]表示索引i右边部分奇偶元素差值,去除索引i后,dp[n] - dp[i]表示索引i右边部分奇偶元素差值的相反数
        # 因此,对任意i,只要dp[i-1] == dp[n] - dp[i],即满足题目要求
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + (-nums[i-1] if i & 1 else nums[i-1])
        #print(dp)

        ans = 0
        for i in range(1, n + 1):
            if dp[i - 1] == dp[n] - dp[i]:
                ans += 1

        return ans

        # 模拟
        '''
        n = len(nums)
        if n == 1:
            return 1
        # 预计算奇数和,偶数和
        s = nums[:2]
        for i in range(2,n):
            s.append(s[-2] + nums[i])
        #print(s)
        ans = 0
        for i in range(n):
            #print(i,n,nums[i])
            if (i ^ n) & 1:   # i和n不同奇偶
                #print((s[i - 1] if i > 0 else 0),s[n - 1],s[i],(s[i - 2] if i > 1 else 0),s[n - 2],(s[i - 1] if i > 0 else 0))
                one = (s[i - 1] if i > 0 else 0) + s[n - 1] - s[i]
                two = (s[i - 2] if i > 1 else 0) + s[n - 2] - (s[i - 1] if i > 0 else 0)
            else:   # i和n同奇偶
                #print((s[i - 1] if i > 0 else 0),s[n - 2],s[i],(s[i - 2] if i > 1 else 0),s[n - 1],(s[i - 1] if i > 0 else 0))
                one = (s[i - 1] if i > 0 else 0) + s[n - 2] - s[i]
                two = (s[i - 2] if i > 1 else 0) + s[n - 1] - (s[i - 1] if i > 0 else 0)
            #print(one,two)
            if one == two:
                ans += 1
        return ans
        '''