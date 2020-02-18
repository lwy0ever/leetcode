class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        base = 1
        while num >= base:
            if (num // base) % 10 == 6:
                ans = num + base * 3
            base *= 10
        return ans