class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        mask = 2 ** k - 1
        m = [0] * 2 ** k
        cur = int(s[:k],2)
        m[cur] = 1
        #print(cur)
        for i in range(k,n):
            if s[i] == '1':
                cur = ((cur << 1) + 1) & mask
            else:
                cur = (cur << 1) & mask
            #print(cur)
            m[cur] = 1
        return all(x == 1 for x in m)