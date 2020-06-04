class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x,y):
            if x % y == 0:
                return y
            return gcd(y,x % y)

        ans = []
        for i in range(2,n + 1):    # 分母
            for j in range(1,i):    # 分子
                if gcd(i,j) == 1:
                    ans.append('%d/%d' % (j,i))
        return ans