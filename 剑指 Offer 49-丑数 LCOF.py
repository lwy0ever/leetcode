class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 优化算法
        # 一个丑数,一定是之前的某个丑数x2,x3,x5得到的
        primes = [2,3,5]
        pn = len(primes)
        ans = [1]
        ind = [0] * pn   # 记录将要被primes乘的数在ans里面的位置
        for _ in range(n - 1):
            arr = [ans[ind[i]] * primes[i] for i in range(pn)]
            _min = min(arr)
            for i in range(pn):
                if _min == arr[i]:  # ind[i]是被选中的点,ind[i]后移.一次可能同时选中多个点
                    ind[i] += 1
            ans.append(_min)
            #print(ans,ind)
        return ans[-1]
        
        '''
        # 原算法
        # 一个丑数,一定是之前的某个丑数x2,x3,x5得到的
        primes = [2,3,5]
        pn = len(primes)
        ans = [1]
        ind = [0] * pn   # 记录将要被primes乘的数在ans里面的位置
        for _ in range(n - 1):
            _min = float('inf')
            for i in range(pn):
                _min = min(_min,ans[ind[i]] * primes[i])
            for i in range(pn):
                if _min == ans[ind[i]] * primes[i]:  # ind[i]是被选中的点,ind[i]后移.一次可能同时选中多个点
                    ind[i] += 1
            ans.append(_min)
            #print(ans,ind)
        return ans[-1]
        '''