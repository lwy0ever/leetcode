class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 位运算
        # 类似于3进制
        # 00 -> 01 -> 10 -> 00
        # 用one表示低位,two表示高位
        # one的变化可以表示为one ^ num & ~two
        # two的变化表示表示为two ^ num & ~one(这里的one,是已经变化以后的one)
        # 运算优先级~ > & > ^
        one, two = 0, 0
        for num in nums:
            #print(bin(num),bin(one),bin(two))
            one = one ^ num & ~two
            two = two ^ num & ~one
        #print(bin(num),bin(one),bin(two))
        return one