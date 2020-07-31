class Solution:\u000A    def numOfSubarrays(self, arr: List[int]) \u002D\u003E int:\u000A        # 内存优化\u000A        # 子数组要求是连续数组\u000A        n \u003D len(arr)\u000A        ans \u003D 0\u000A        even \u003D 0    # even表示选择arr[i]的偶数和子数组个数\u000A        odd \u003D 0     # odd表示选择arr[i]的奇数和子数组个数\u000A        for i in range(n):\u000A            if arr[i] \u0026 1:\u000A                even,odd \u003D odd,even + 1 # 偶数和子数组+arr[i] or arr[i]自身\u000A            else:\u000A                even \u003D even + 1 # 偶数和子数组+arr[i] or arr[i]自身\u000A                #odd \u003D odd\u000A            ans +\u003D odd\u000A        #print(dp[0])\u000A        #print(dp[1])\u000A        return ans % (10 ** 9 + 7)\u000A\u000A        \u0027\u0027\u0027\u000A        # 子数组要求是连续数组\u000A        n \u003D len(arr)\u000A        ans \u003D 0\u000A        # dp[0][i + 1]表示选择arr[i]的偶数和子数组个数\u000A        # dp[1][i + 1]表示选择arr[i]的奇数和子数组个数\u000A        dp \u003D [[0] * (n + 1) for _ in range(2)]\u000A        for i in range(n):\u000A            if arr[i] \u0026 1:\u000A                dp[0][i + 1] \u003D dp[1][i]\u000A                dp[1][i + 1] \u003D dp[0][i] + 1 # 偶数和子数组+arr[i] or arr[i]自身\u000A            else:\u000A                dp[0][i + 1] \u003D dp[0][i] + 1 # 偶数和子数组+arr[i] or arr[i]自身\u000A                dp[1][i + 1] \u003D dp[1][i]\u000A            ans +\u003D dp[1][i + 1]\u000A        #print(dp[0])\u000A        #print(dp[1])\u000A        return ans % (10 ** 9 + 7)\u000A        \u0027\u0027\u0027