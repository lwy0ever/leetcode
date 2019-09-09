class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        pn = len(primes)
        ind = [0] * pn  # 记录与primes[i]相乘的丑数在丑数序列中的索引
        ans = [1]   # 丑数序列 第一个丑数为1
        for i in range(1,n):
            ans.append(min([ans[ind[j]] * primes[j] for j in range(pn)]))   # 下一个丑数的可能值,取最小的一个
            for j in range(pn):
                if ans[-1] == ans[ind[j]] * primes[j]:  # 索引指向丑数序列中的下一个丑数
                    ind[j] += 1
        return ans[-1]
