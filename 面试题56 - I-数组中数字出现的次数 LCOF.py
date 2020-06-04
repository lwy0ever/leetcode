class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        for n in nums:
            s ^= n
        # s是全员异或
        # 假设结果为a,b
        # 那么s中的1,表示a和b二进制不同数位
        # 找到任意一位就可以将数组分成2部分,一部分含a,一部分含b,其余相同的数字在同一组
        bit = 1
        while bit & s == 0:
            bit <<= 1
        a = 0
        b = 0
        for n in nums:
            if n & bit:
                a ^= n
            else:
                b ^= n
        return [a,b]