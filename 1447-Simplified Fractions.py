class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            if a < b:
                a,b = b,a
            while b != 0:
                t = a % b
                a = b
                b = t
            return a
        
        ans = []
        for i in range(1,n + 1):
            for j in range(1,i):
                if gcd(i,j) > 1:
                    continue
                ans.append(f'{j}/{i}')
        return ans