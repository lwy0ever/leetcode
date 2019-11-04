class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        stack = []  # 记录左括号的位置
        anslength = 0   # 记录ans的长度
        for i,c in enumerate(s):
            if c == '(':
                ans.append(c)
                stack.append(anslength)
                anslength += 1
            elif c == ')':
                if stack:
                    ans.append(c)
                    stack.pop()
                    anslength += 1
                else:
                    continue
            else:
                ans.append(c)
                anslength += 1
        while stack:
            p = stack.pop()
            ans.pop(p)
        return ''.join(ans)