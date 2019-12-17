class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # print(bin(ord('A')))
        # 0b1000001
        # print(bin(ord('C')))
        # 0b1000011
        # print(bin(ord('G')))
        # 0b1000111
        # print(bin(ord('T')))
        # 0b1010100
        di = set()
        ans = set()
        s9 = s[:9]
        t = 0
        for c in s9:
            t <<= 2
            t += (ord(c) >> 1) & 3
            #print(bin(t))
        n = len(s)
        mm = 0xfffff
        for i in range(9,n):
            t <<= 2
            t += (ord(s[i]) >> 1) & 3
            t &= mm
            #print(bin(t))
            if t not in di:
                di.add(t)
            else:
                ans.add(s[i - 9:i + 1])
        return list(ans)