class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ma = [float('-inf'),float('-inf'),float('-inf')]
        for n in nums:
            if n > ma[2]:
                if n > ma[1]:
                    if n > ma[0]:
                        ma[1:3] = ma[0:2]
                        ma[0] = n
                    elif n < ma[0]:
                        ma[2] = ma[1]
                        ma[1] = n
                elif n < ma[1]:
                    ma[2] = n
        if ma[2] > float('-inf'):
            return ma[2]
        else:
            return ma[0]