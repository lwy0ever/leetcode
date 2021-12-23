class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.i = 0
        self.n = len(s)
        def helper(reverse):
            #print('call',i,reverse)
            ans = []
            while self.i < self.n:
                #print(i,reverse)
                if s[self.i] == '(':
                    self.i += 1
                    x = helper(-reverse)
                    #print(x)
                    if reverse:
                        ans += x[::-1]
                    else:
                        ans += x
                    #print(ans)
                elif s[self.i] == ')':
                    self.i += 1
                    return ans
                else:
                    ans.append(s[self.i])
                    self.i += 1
            return ans
        ans = helper(-1)
        return ''.join(ans)