class Solution:
    def reformat(self, s: str) -> str:
        ans = []
        stack = []
        for c in s:
            if ans and ans[-1].isalpha() == c.isalpha():
                if stack and (ans[-1].isalpha() != stack[-1].isalpha()):
                    ans.append(stack.pop())
                    ans.append(c)
                else:
                    stack.append(c)
            else:
                ans.append(c)
            #print(ans,stack)
        if stack:
            if len(stack) == 1:
                if stack[0].isalpha() != ans[-1].isalpha():
                    ans.append(stack.pop())
                    return ''.join(ans)
                if stack[0].isalpha() != ans[0].isalpha():
                    ans.insert(0,stack.pop())
                    return ''.join(ans)
                return ''
            else:
                return ''
        return ''.join(ans)