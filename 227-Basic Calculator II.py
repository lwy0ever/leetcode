class Solution:
    def calculate(self, s: str) -> int:
        s = s + '+0'
        #print(s)
        val = [0]   # 数值入栈
        op = ['+']    # 操作符入栈
        tmp = 0
        for c in s:
            if c in ('+','-','*','/'):
                if op[-1] == '*': # 优先级最高,直接计算
                    val[-1] *= tmp
                    op[-1] = c
                elif op[-1] == '/': # 优先级最高,直接计算
                    val[-1] //= tmp
                    op[-1] = c
                else:
                    val.append(tmp)
                    op.append(c)
                tmp = 0
            elif c.isdigit():
                tmp = tmp * 10 + int(c)
        val.append(tmp)
        #print(val,op)
        ans = val[0]
        for i in range(len(op)):
            if op[i] == '+':
                ans += val[i + 1]
            else:
                ans -= val[i + 1]
        return ans