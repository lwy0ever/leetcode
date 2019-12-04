class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 模拟不需要进位的3进制
        one = two = three = 0
        for n in nums:
            two |= one & n # 二进制某位出现1次时two = 0,出现2,3次时two = 1
            one ^= n  # 二进制某位出现2次时one = 0,出现1,3次时one = 1
            three = one & two # 二进制某位出现3次时（即two = one = 1时）three = 1,其余即出现1,2次时three = 0
            one &= ~three # 将出现3次的位置清零
            two &= ~three
        return one