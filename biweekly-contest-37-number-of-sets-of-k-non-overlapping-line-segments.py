class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        '''
        # 方法1
        # factorial是阶乘
        # n个点,连接出k条线段
        # 题目要求线段可以相连,那么我们在每条线段(最后一条除外)的后面加一个点
        # 比如5个点,0,1,2,3,4中有2条线段,[1,2],[3,4],则将点变成0,1,2,2,3,4
        # 如果线段是[1,2],[2,3],就不会有相邻的感觉了
        # 所以,将n个点,加成n + k - 1个点(这k - 1个点是先有线段,然后才追加的点)
        # 在这n + k - 1个点中任选2k个点组成线段
        import math
        return math.comb(n + k - 1,k * 2) % (10 ** 9 + 7)
        return math.factorial(n + k - 1) // math.factorial(k * 2) // math.factorial(n - k - 1) % (10 ** 9 + 7)
        '''

        # 方法2
        # dp[len][num]表示前len个点,形成num个线段的方案数
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # dpLast[len][num]表示前len个点,形成num个线段的方案数,其中最后一个线段的结尾是最后一个点
        dpLast = [[0] * (k + 1) for _ in range(n + 1)]
        for l in range(2,n + 1):
            dp[l][0] = 1
            dp[l][1] = l * (l - 1) // 2
            dpLast[l][1] = l - 1
        for num in range(2,k + 1):
            dp[num + 1][num] = 1
            dpLast[num + 1][num] = 1
            for l in range(num + 1,n + 1):
                # 2种方式
                # 1,取l - 1个点,从1到l - 1,组成num个线段(取结尾点)
                # 2,取l - 1个点,从0到l - 2,组成num - 1个线段(不限制结尾点),加1个线段[l-2,l-1]
                dpLast[l][num] = dpLast[l - 1][num] + dp[l - 1][num - 1]
                # 2种方式
                # 1,取l - 1个点,从0到l - 2,组成num个线段(不限制结尾点),加空点l - 1
                # 2,取l个点,从0到l - 1,组成num个线段(取结尾点)
                dp[l][num] = dp[l - 1][num] + dpLast[l][num]
        return dp[n][k] % (10 ** 9 + 7)