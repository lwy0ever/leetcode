class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 第i个灯泡从最初状态到最后操作完毕,被操作的次数等价于i的约数个数
        # 如果灯最终是亮着的,则说明i有奇数个约数
        # -->问题转化为求那几个数有奇数个约数:
        # 一个数如果有奇数个约数,则这个数肯定是个完全平方数
        # 1-n中是完全平方数的数的个数为int(n ** 0.5)
        return int(n ** 0.5)
        '''
        if n == 0:
            return 0
        ans = 1
        for i in range(2,n + 1):    # i = 1,必然是on
            t = 0
            for m in range(2,i):    # 由于i >= 2,所以m = 1和m = i必然造成一次on,一次off,不需要再考虑
                if i % m == 0:
                    t ^= 1
            if t:
                ans += 1
        return ans
        '''