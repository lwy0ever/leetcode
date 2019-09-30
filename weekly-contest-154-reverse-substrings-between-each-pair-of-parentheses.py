class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = ''
        #print(s)
        n = len(s)
        cnt = 0
        l = 0
        r = 0
        for i in range(n):
            if s[i] == '(':
                if cnt == 0:
                    l = i
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
                if cnt == 0:
                    #print(l,i,s[i - 1:l:-1])
                    ans += self.reverseParentheses(s[i - 1:l:-1].replace('(','|').replace(')','(').replace('|',')'))
            elif cnt == 0:
                ans += s[i]
                #print(ans)
        return ans
                    