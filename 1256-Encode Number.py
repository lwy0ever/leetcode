class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ''
        ans = ''
        l = 0
        while num >= (1 << l):
            num -= (1 << l)
            l += 1
        #print(l)
        ans = bin(num)[2:].zfill(l)
        return ans