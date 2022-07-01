class Solution:
    def trailingZeroes(self, n: int) -> int:
        # n!出现0,说明有2和5
        # 2出现的次数一定多于5,所以关心5出现的次数
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans