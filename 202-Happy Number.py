class Solution:
    def isHappy(self, n: int) -> bool:
        appeared = set()
        while n != 1:
            appeared.add(n)
            newN = 0
            while n:
                n,m = divmod(n,10)
                newN += m ** 2
            n = newN
            #print(n)
            if n == 1:
                return True
            if n in appeared:
                return False
        return True