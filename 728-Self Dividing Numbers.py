class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(n):
            d = n
            while d:
                d,m = divmod(d,10)
                if m == 0:
                    return False
                if n % m != 0:
                    return False
            return True
        
        ans = []
        for i in range(left,right + 1):
            if check(i):
                ans.append(i)
        return ans