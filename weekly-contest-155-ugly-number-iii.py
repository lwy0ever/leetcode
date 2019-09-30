class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcd(x,y):   #求最大公约数
            if y==0:
                return x
            return lcd(y,x%y)
        
        ab = a * b // lcd(a,b)
        ac = a * c // lcd(a,c)
        bc = b * c // lcd(b,c)
        
        abc = ab * c // lcd(ab,c)
                
        #print(ab,ac,bc,abc)
        def getDivNum(x): # [0,x]中整除的数的个数
            return x//a + x//b + x//c - x//ab - x//ac - x//bc + x//abc
        
        
        
        l,r = 0, 2000000000
        while l < r:
            mid = (l+r)//2
            num = getDivNum(mid)
            if num == n:
                r = mid #需要找到满足 getDivNum(mid) == n的最小的一个
            elif num < n:
                l = mid +1
            else:
                r = mid -1
        return l