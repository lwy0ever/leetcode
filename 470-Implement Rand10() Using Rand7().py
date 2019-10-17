# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        t1 = rand7()
        while t1 == 4:
            t1 = rand7()
        ans = 0
        if t1 < 4:
            ans = 0
        else:
            ans = 5
        t2 = rand7()
        while t2 >= 6:
            t2 = rand7()
        ans += t2
        return ans