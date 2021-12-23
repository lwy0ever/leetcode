class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # 最大数是10 ** 18
        # len(bin(10 ** 18)) = 62,所以最多是60个1
        ans = float('inf')
        n = int(n)
        
        def check(m,length):
            ret = 1
            mul = 1
            for i in range(length):
                mul *= m
                ret += mul
            return ret
            
        for i in range(1,61):    # i表示1的个数
            l = 2   # 最小为2进值
            r = n   # 最大为n - 1进值
            while l < r:
                m = (l + r) // 2
                rt = check(m,i)
                if rt == n:
                    ans = min(ans,m)
                    break
                elif rt < n:
                    l = m + 1
                else:
                    r = m
        return str(ans)