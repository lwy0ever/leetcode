class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1位数,9个(不含0),1到9
        # 2位数,90个,10到99
        # 3位数,900个,100到999
        # ...
        num = 9
        length = 1
        while n > num * length:
            n -= num * length
            num *= 10
            length += 1
        # 经过上面的计算,n表示在长度为length的数字中的位置
        a = n // length # 表示第几个数字
        b = n % length  # 表示数字的第几位
        if b == 0:
            b = length
        base = 10 ** (length - 1)
        if b == length:
            ans = base + a - 1
        else:
            ans = base + a
        return ans // (10 ** (length - b)) % 10
        #return str(ans)[b - 1]