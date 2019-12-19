class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        n = len(s)

        def cal(start):
            ans = 0
            lastOp = 1
            tmp = 0
            i = start
            while i < n:
                if s[i] in('+','-'):
                    ans += tmp * lastOp
                    tmp = 0
                    if s[i] == '+':
                        lastOp = 1
                    else:
                        lastOp = -1
                elif s[i] == '(':
                    #print(s,i)
                    tmp,newStart = cal(i + 1)
                    ans += tmp * lastOp
                    tmp = 0
                    i = newStart
                    continue
                elif s[i] == ')':
                    ans += tmp * lastOp
                    #print(s[start:],ans)
                    return ans,i + 1
                else:
                    tmp = tmp * 10 + int(s[i])
                i += 1
            ans += tmp * lastOp
            #print(s[start:],ans)
            return ans,i
        
        return cal(0)[0]