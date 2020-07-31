class Solution:
    def fib(self, n: int) -> int:
        # 节省内存写法
        if n == 0:
            return 0
        f = [0,1]
        i = 1
        while i < n:
            f = [f[-1],f[-2] + f[-1]]
            i += 1
        return f[1] % (10 ** 9 + 7)
    
        '''
        f = [0,1]
        i = 1
        while i < n:
            f.append(f[-2] + f[-1])
            i += 1
        return f[n] % (10 ** 9 + 7)
        '''