class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def valid(a,b,i):   # 已有a,b,从num[i:]开始检查是否满足要求
            #print(a,b,num[i:])
            if i == len(num):
                return True
            c = a + b
            l = len(str(c))
            if c == int(num[i:i + l]):
                return valid(b,c,i + l)
            else:
                return False

        n = len(num)
        if n < 3:
            return False
        # 重点是找到第1和第2个数字:num[:i]和num[i:j]
        if num[0] == '0':
            lastI = 2
        else:
            lastI = n - 1
        for i in range(1,lastI):
            a = int(num[:i])
            if num[i] == '0':
                lastJ = i + 2
            else:
                lastJ = n
            for j in range(i + 1,lastJ):
                b = int(num[i:j])
                #print(a,b)
                if valid(a,b,j):
                    return True
        return False