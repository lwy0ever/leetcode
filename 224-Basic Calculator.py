class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        n = len(s)

        # 从字符串的第start位开始计算
        # 返回结果和本次计算到达的位数
        def cal(start):
            ans = 0
            lastOp = 1
            tmp = 0
            i = start
            while i < n:
                if s[i] in('+','-'):    # 计算
                    ans += tmp * lastOp
                    tmp = 0
                    if s[i] == '+':
                        lastOp = 1
                    else:
                        lastOp = -1
                elif s[i] == '(':   # 左括号,相当于一个新的计算
                    #print(s,i)
                    tmp,newStart = cal(i + 1)
                    ans += tmp * lastOp
                    tmp = 0
                    i = newStart
                    continue
                elif s[i] == ')':   # 右括号,返回计算结果
                    ans += tmp * lastOp
                    #print(s[start:],ans)
                    return ans,i + 1
                else:   # 数字
                    tmp = tmp * 10 + int(s[i])
                i += 1
            ans += tmp * lastOp
            #print(s[start:],ans)
            return ans,i
        
        return cal(0)[0]