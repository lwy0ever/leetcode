class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        needDigital = True
        needLower = True
        needUpper = True
        for c in s:
            if c.isdigit():
                needDigital = False
            elif c.islower():
                needLower = False
            elif c.isupper():
                needUpper = False
        missed = needDigital + needLower + needUpper
        #print(missed)
        # 处理连续字符
        # 替换效率最高.n个(n >= 3)连续字符,需要n // 3次替换
        # 插入效率居中.n个(n >= 3)连续字符,需要(n - 1) // 2次插入
        # 删除效率最低.n个(n >= 3)连续字符,需要n - 2次删除
        # 一般情况下,如果使用替换的方式,需要n // 3次替换
        # 当长度超过20时,应该尽可能用删除的方式
        # 在n % 3 == 0时,需要n // 3次替换,如果用1次删除,则需要替换的次数-1
        # 在n % 3 == 1时,需要n // 3次替换,如果用2次删除,则需要替换的次数-1
        n = len(s)
        delOne = 0
        delTwo = 0
        replace = 0
        pre = ''
        cnt = 0
        for c in s:
            if c == pre:
                cnt += 1
            else:
                pre = c
                if cnt >= 3:
                    if cnt % 3 == 0:
                        delOne += 1
                    if cnt % 3 == 1:
                        delTwo += 1
                    replace += cnt // 3
                cnt = 1
        if cnt >= 3:
            if cnt % 3 == 0:
                delOne += 1
            if cnt % 3 == 1:
                delTwo += 1
            replace += cnt // 3
        
        #print(missed,replace)
        ans = 0
        if n < 6:
            return max(6 - n,missed)
        elif n <= 20:
            return max(replace,missed)
        else:   # n > 20
            toDel = n - 20
            # 下面这块没明白
            # Each deletion can represent one replacement.
            replace -= min(toDel,delOne)
            if toDel - delOne > 0:
                replace -= min((toDel - delOne) // 2,delTwo)
            if toDel - delOne - 2 * delTwo > 0:
                replace -= (toDel - delOne - 2 * delTwo) // 3
            return toDel + max(replace,missed)