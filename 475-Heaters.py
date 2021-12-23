class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 计算每个房子能找到的最近的供暖器
        n = len(heaters)
        heaters.sort()
        ans = 0
        for house in houses:
            p = bisect.bisect(heaters,house)
            minDis = float('inf')  # 表示该房子需要的最小供暖器半径
            if 0 <= p < n and heaters[p] == house: # 房子和供暖器位置重叠
                minDis = 0
            else:
                if p - 1 >= 0:  # 左侧有供暖器
                    minDis = min(minDis,house - heaters[p - 1])
                if p < n:   # 右侧有供暖器
                    minDis = min(minDis,heaters[p] - house)
            ans = max(ans,minDis)
        return ans