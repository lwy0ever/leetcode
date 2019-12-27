class Solution:
    def numberToWords(self, num: int) -> str:
        # 2 ** 31,共10位
        # 9位分一堆,然后3位分一堆
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def ntw(n):
            if n < 20:
                return to19[n - 1:n]    # 返回to19[n - 1:n]而不是to19[n - 1],可以有效处理n = 0的情况
            if n < 100:
                return [tens[n // 10 - 1]] + ntw(n % 10)
            if n < 1000:
                return [to19[n // 100 - 1]] + ['Hundred'] + ntw(n % 100)
            if n >= 10 ** 9:
                return ntw(n // (10 ** 9)) + ['Billion'] + ntw(n % (10 ** 9))
            if n >= 10 ** 6:
                return ntw(n // (10 ** 6)) + ['Million'] + ntw(n % (10 ** 6))
            if n >= 10 ** 3:
                return ntw(n // (10 ** 3)) + ['Thousand'] + ntw(n % (10 ** 3))
        
        return ' '.join(ntw(num)) or 'Zero'