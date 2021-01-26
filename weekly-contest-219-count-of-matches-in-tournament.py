class Solution:
    def numberOfMatches(self, n: int) -> int:
        # 每次比赛都需要1次配对
        # 从n个队伍淘汰n-1个,需要n-1次比赛
        return n - 1