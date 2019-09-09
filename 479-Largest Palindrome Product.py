class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        ma = 10 ** n - 1
        left = 10 ** n - 1
        while left >= 10 ** (n - 1):
            right = str(left)[::-1]
            #print(right)
            pali = int(str(left) + right)
            for i in range(ma if pali % 2 == 0 else ma // 2 * 2 + 1,int(pali ** 0.5),-1 if pali % 2 == 0 else -2):
                if pali % i == 0:
                    #print('a')
                    return pali % 1337
            left -= 1
