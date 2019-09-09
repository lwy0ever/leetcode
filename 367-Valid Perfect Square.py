class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num + 1
        while l < r:
            mid = (l + r) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            elif tmp < num:
                l = mid + 1
            else:
                r = mid
        return False
        '''
        if num == 1:
            return True
        t = 2
        r = num // t
        while t + 1 < r or r + 1 < t:
            #print(t,r)
            t = (t + r) // 2
            r = num // t
        return True if t * t == num else False
        '''