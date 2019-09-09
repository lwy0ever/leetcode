class Solution:
    def myAtoi(self, str: str) -> int:
        ans = 0
        sign = 1
        blanked = False
        signed = False
        for c in str:
            if c == ' ':
                if blanked:
                    return ans
                else:
                    continue
            else:
                blanked = True
            if c == '-':
                if not signed:
                    sign = -1
                    signed = True
                    continue
                else:
                    return ans
            if c == '+':
                if not signed:
                    signed = True
                    continue
                else:
                    return ans
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                signed = True
                #print(c,ans)
                ans = ans * 10 + (ord(c) - ord('0')) * sign
                ans = min(ans,2 ** 31 - 1)
                ans = max(ans,- 2 ** 31)
            else:
                return ans
        return ans