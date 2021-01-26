class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        towers.sort()
        maxX = max(t[0] for t in towers)
        maxY = max(t[1] for t in towers)
        # 信号最强的点,应该在(0,0)-(maxX,maxY)范围内
        ans = None
        _max = -1
        for x in range(maxX + 1):
            for y in range(maxY + 1):
                sumq = 0
                for fx,fy,fq in towers:
                    d = ((fx - x) ** 2 + (fy - y) ** 2) ** 0.5
                    if d <= radius:
                        sumq += int(fq / (1 + d))
                if sumq > _max:
                    ans = [x,y]
                    _max = sumq
        return ans