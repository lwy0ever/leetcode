class Solution:
    def canWinNim(self, n: int) -> bool:
        # n % 4 = 0的情况下,1+3=2+2=3+1,后手胜
        # n % 4 != 0的情况下,先手拿n % 4个,转化为后手胜
        return n % 4