class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        t = x
        while t > 0:
            t,m = divmod(t,10)
            reverse = reverse * 10 + m
        #print(reverse)
        return reverse == x        