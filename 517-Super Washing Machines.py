class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n > 0:   # 无法均分
            return -1
        avg = total // n
        # n台洗衣机,每次移动都是发生在相邻洗衣机之间
        # 将前i台和后n - i台分成2组,则两组之间的移动次数=abs(avg * i - sum[:i]),每组之间都是如此
        # 还需要注意,可能存在某台洗衣机,需要向2侧移动的情况
        pre = 0
        ans = 0
        for m in machines:
            m -= avg    # 本台洗衣机需要移出的总量
            pre += m    # 前i台组成的洗衣机组需要移动的数量
            ans = max(ans,abs(pre),m)
        return ans