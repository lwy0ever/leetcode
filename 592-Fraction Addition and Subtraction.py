class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = re.findall(r'([+-]?)(\d+)/(\d+)',expression)
        #print(l)
        l = [[1 if x[0] in ('','+') else -1,int(x[1]),int(x[2])] for x in l]
        
        def gcd(x,y):
            while x % y > 0:
                _,x = divmod(x,y)
                x,y = y,x
            return y
        
        ans = l[0]
        for sign,a,b in l[1:]:
            if ans[1] == 0:
                ans = [sign,a,b]
            else:
                m = gcd(ans[2],b)
                ans = [1,ans[0] * ans[1] * b // m + sign * a * ans[2] // m,ans[2] * b // m]
                #print(ans)
        if ans[1] < 0:
            ans[0] = -ans[0]
            ans[1] = -ans[1]
        elif ans[1] == 0:
            ans[0] = 1
            ans[2] = 1
        if ans[1] != 0 and ans[2] != 0:
            m = gcd(abs(ans[1]),ans[2])
            ans[1] //= m
            ans[2] //= m
        return str(ans[0] * ans[1]) + '/' + str(ans[2])