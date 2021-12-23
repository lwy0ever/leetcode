class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 类似3进制
        # ones ^= num：记录至目前元素num，二进制某位出现 1 次（当某位出现 3 次时有 ones = 1，与 twos = 1 共同表示“出现 3 次”）
        # twos |= ones & num：记录至目前元素num，二进制某位出现 2 次 （当某位出现 2 次时，twos = 1 且 ones = 0 ）
        # threes = ones & twos：记录至目前元素num，二进制某位出现 3 次（即当 ones 和 twos 对应位同时为 1 时 three = 1 ）
        # one &= ~threes, two &= ~threes：将 ones, twos 中出现了 3 次的对应位清零，实现 “不考虑进位的三进制加法” 
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # 二进制某位出现1次时twos = 0，出现2, 3次时twos = 1；
            ones ^= num  # 二进制某位出现2次时ones = 0，出现1, 3次时ones = 1；
            threes = ones & twos # 二进制某位出现3次时（即twos = ones = 1时）three = 1，其余即出现1, 2次时three = 0；
            ones &= ~threes # 将二进制下出现3次的位置零，实现`三进制下不考虑进位的加法`；
            twos &= ~threes
        return ones