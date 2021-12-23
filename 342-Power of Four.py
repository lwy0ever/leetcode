class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # num要大于0
        # num的二进制形式应该只含有1个1
        # num的二进制形式长度为奇数
        return num > 0 and (num - 1) & num == 0 and (len(bin(num)) & 1) == 1
        #return num > 0 and (num - 1) & num == 0 and num % 3 == 1