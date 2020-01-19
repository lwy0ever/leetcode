class Solution:
    def countBits(self, num: int) -> List[int]:
        #   0
        #   1
        #  10
        #  11
        # 100
        # 101
        # 110
        # 111
        ans = [0] * (num + 1)
        i = 0
        b = 1
        while b <= num:
            while i < b and b + i <= num:
                ans[b + i] = ans[i] + 1
                i += 1
            b <<= 1
            i = 0
        return ans