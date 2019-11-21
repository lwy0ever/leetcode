class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a)
        nb = len(b)
        toadd = 0
        ans = []
        for i in range(1,max(na,nb) + 1):
            if i <= na:
                ca = int(a[-i])
            else:
                ca = 0
            if i <= nb:
                cb = int(b[-i])
            else:
                cb = 0
            toadd,c = divmod(ca + cb + toadd,2)
            ans.append(c)
        if toadd:
            ans.append(toadd)
        return ''.join(map(str,ans[::-1]))