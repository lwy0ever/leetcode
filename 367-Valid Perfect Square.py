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
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
        '''