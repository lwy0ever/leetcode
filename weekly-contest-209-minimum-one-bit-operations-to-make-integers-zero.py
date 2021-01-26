class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        cache = dict()
        def helper(x):  # 返回x操作到0所需要的最小步数
            if x <= 1:
                return x
            if x in cache:
                return cache[x]
            # 为了变成0,一定需要最高位的1变成0
            # 考虑最高位的1
            # 1,如果次高位是1,也就是11xxx的形式,那么先变成11000,然后使用操作2,将11000变成01000
            # 2,如果次高位是0,也就是10xxx的形式
            #   对于10000,如果要变为01000,需要如下步骤(格雷码?)
            #   10000
            #   10001
            #   10011
            #   10010
            #   10110
            #   10111
            #   10101
            #   10100
            #   11100
            #   11101
            #   11111
            #   11110
            #   11010
            #   11011
            #   11001
            #   11000
            #   01000
            #   可以发现,遍历了所有形式
            #   所以从10xxx变成0,可以分成3步:
            #   a,从10xxx变成11000
            #   b,从11000变成01000
            #   c,从01000变成0
            #   同时可以发现
            #   第1个状态和倒数第1个状态分别是10000和11000
            #   第2个状态和倒数第2个状态分别是10001和11001
            #   第3个状态和倒数第3个状态分别是10011和11011
            #   第4个状态和倒数第4个状态分别是10010和11010
            #   ...类似是对称的
            #   所以0xxx变成1xxx,相当于1000变成0的次数,然后减掉2倍的xxx变成0的次数
            #   所以helper(10xxx) = helper(1000) - helper(xxx) * 2 + helper(11xxx)
            #    = helper(1000) - helper(xxx) * 2 + helper(xxx) + helper(11000)
            #    = helper(1000) - helper(xxx) + helper(11000)
            i = 31
            mask = 2 ** 32 - 1
            while x & (mask >> i << i) == 0:
                i -= 1
            #print(i,mask)
            # i表示x的最高位(比如1xxx,则i=4)
            if 1 << (i - 1) & x:    # 次高位是1
                cache[x] = helper(x ^ (3 << (i - 1))) + 1 + helper(1 << (i - 1))
            else:
                cache[x] = helper(1 << (i - 1)) - helper(x ^ (1 << i)) + helper(3 << (i - 1))
            return cache[x]
        return helper(n)