class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        #print(expression)
        if expression == 't':
            return True
        if expression == 'f':
            return False
        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])
        s = ''
        cnt = 0
        for c in expression[2:-1]:
            if c == ',' and cnt == 0:
                b = self.parseBoolExpr(s)
                #print(expression,s,b)
                s = ''
                if expression[0] == '&' and not b:
                    return False
                if expression[0] == '|' and b:
                    return True
            else:
                s += c
                if c == '(':
                    cnt += 1
                if c == ')':
                    cnt -= 1
        else:
            b = self.parseBoolExpr(s)
            # 之前的表达式均无法直接返回，所以最后一个表达式将直接决定结果
            if b:
                return True
            else:
                return False
                    
            