class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        r = 1   # 表示要加的数字(or进位)
        i = 1
        while r > 0 and i <= n:
            r,digits[-i] = divmod(digits[-i] + r,10)
            i += 1
        if r > 0:
            digits.insert(0,r)
        return digits