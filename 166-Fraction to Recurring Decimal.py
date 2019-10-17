class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        # 处理负数
        if numerator * denominator < 0:
            ans += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        # 整数部分
        z,m = divmod(numerator,denominator)
        if m == 0:
            return ans + str(z)
        ans += str(z) + '.'
        # 思路:使用竖式除法,除不尽就乘以10,直到整除or出现循环
        fraction = '' # 小数部分
        appeared = [] # 出现过的小数
        while True:
            m *= 10
            d,m = divmod(m,denominator)
            #print(ans,fraction,appeared,d,m)
            if (d,m) in appeared:
                pos = appeared.index((d,m))
                return ans + fraction[:pos] + '(' + fraction[pos:] + ')'
            fraction += str(d)
            if m == 0:
                return ans + fraction
            appeared.append((d,m))
            