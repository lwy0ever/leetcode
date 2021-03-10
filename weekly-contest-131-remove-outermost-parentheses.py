class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        counter = 0
        ans = ''
        j = 0
        for i in range(len(S)):
            if S[i] == '(':
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                ans += S[j + 1:i]
                j = i + 1
        return ans
        '''
        counter = 0
        ans = ''
        for c in S:
            if c == '(':
                if counter > 0:
                    ans += c
                counter += 1
            elif c == ')':
                if counter > 1:
                    ans += c
                counter -= 1
        return ans
        '''
