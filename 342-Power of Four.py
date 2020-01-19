class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num - 1) & num == 0 and len(bin(num)) % 2 == 1
        #return num > 0 and (num - 1) & num == 0 and num % 3 == 1