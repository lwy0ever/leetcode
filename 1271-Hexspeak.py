class Solution:
    def toHexspeak(self, num: str) -> str:
        n = hex(int(num))[2:].upper().replace('1','I').replace('0','O')
        for c in n:
            if c not in ('A','B','C','D','E','F','I','O'):
                return 'ERROR'
        return n