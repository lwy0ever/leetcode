class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+','-','*','/'):
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    tmp = a + b
                elif t == '-':
                    tmp = a - b
                elif t == '*':
                    tmp = a * b
                elif t == '/':
                    tmp = int(a / b)
                stack.append(tmp)
            else:
                stack.append(int(t))
        return stack[-1]