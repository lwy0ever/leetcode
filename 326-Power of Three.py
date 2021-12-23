class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0 and n % 3 == 0:
                n //= 3
        return n == 1

        return n > 0 and 3 ** round(math.log(n, 3)) == n