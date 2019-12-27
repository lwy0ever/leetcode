class Solution:
    def numSquares(self, n: int) -> int:
        # 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。 推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=(4^a) * (8b+7)
        # 任何正整数都可以拆分成不超过4个数的平方和 ---> 答案只可能是1,2,3,4
        # 如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7) ---> 因此可以先看这个数是否满足上述公式，如果不满足，答案就是1,2,3了
        # 如果这个数本来就是某个数的平方，那么答案就是1，否则答案就只剩2,3了
        # 如果答案是2，即n=a^2+b^2，那么我们可以枚举a，来验证，如果验证通过则答案是2
        # 只能是3
        # ans = 1的情况
        if int(n ** 0.5) ** 2 == n:
            return 1
        # ans = 4的情况
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        # ans = 2的情况
        a = 0
        while a ** 2 <= n: 
            b = int((n - a ** 2) ** 0.5) 
            if a ** 2 + b ** 2 == n: 
                return 2
            a += 1 
        return 3
        '''
        dp = [i for i in range(n + 1)]
        for i in range(2,n + 1):
            for q in range(1,int(i ** 0.5) + 1):
                dp[i] = min(dp[i],1 + dp[i - q * q])
        return dp[n]
        '''