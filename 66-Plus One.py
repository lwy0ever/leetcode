class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        r = (1,0)
        i = 1
        while r[0] == 1 and i <= n:
            r = divmod(digits[-i] + r[0],10)
            digits[-i] = r[1]
            i += 1
        if r[0] == 1:
            digits.insert(0,r[0])
        return digits