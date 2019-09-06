class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        increase = True
        decreasePos = 0
        astr = ''
        for i in range(len(s) - 1):
            if s[i] < s[i + 1]:
                decreasePos = i + 1
                continue
            if s[i] > s[i + 1]:
                increase = False
                break
        if increase:
            return N
        for i in range(len(s)):
            if i < decreasePos:
                    astr += s[i]
            elif i == decreasePos:
                    astr += chr(ord(s[i]) - 1)
            else:
                astr += '9'
        return int(astr)