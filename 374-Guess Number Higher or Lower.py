# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n + 1
        while l < r:
            t = (l + r) // 2
            rt = guess(t)
            if rt == 0:
                return t
            elif rt == 1:
                l = t + 1
            else:
                r = t