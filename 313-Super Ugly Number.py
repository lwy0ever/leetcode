class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pn = len(primes)
        ind = [0] * pn  # 记录与primes[i]相乘的丑数在丑数序列中的索引
        res = [1]   # 丑数序列 第一个丑数为1
        for i in range(1, n):
            #print(ind)
            #print([res[ind[j]] for j in range(pn)])
            res.append(min([res[ind[j]] * primes[j] for j in range(pn)]))   # 下一个丑数的可能值,取最小的一个
            #print(res)
            for j in range(pn):
                if res[-1] == res[ind[j]] * primes[j]:  # 索引指向丑数序列中的下一个丑数
                    ind[j] += 1
        return res[-1]        