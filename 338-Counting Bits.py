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
        # 1xxx相比于xxx,多1个1
        # 考虑1,比0多1个1
        # 考虑2..3,比0..1各多1个1
        # 考虑4..7,比0..3各多1个1
        # ...
        ans = [0] * (num + 1)
        b = 1
        while b <= num:
            i = 0
            while i < b and b + i <= num:
                ans[b + i] = ans[i] + 1
                i += 1
            b <<= 1
        return ans