class Solution:
    def countAndSay(self, n: int) -> str:
        lastStr = '1'
        if n == 1:
            return lastStr
        for _ in range(n - 1):
            lc = lastStr[0]
            cnt = 1
            newstr = ''
            for i in range(1,len(lastStr)):
                if lastStr[i] != lc:
                    newstr += str(cnt) + lc
                    lc = lastStr[i]
                    cnt = 1
                else:
                    cnt += 1
            lastStr = newstr + str(cnt) + lc
        return lastStr