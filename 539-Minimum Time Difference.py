class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = set()
        for tStr in timePoints:
            h,m = tStr.split(':')
            tspan = int(h) * 60 + int(m)
            if tspan in t:
                return 0
            t.add(tspan)
        ans = 60 * 24
        day = 60 * 24
        # 半天=60*12
        midDay = 60 * 12
        tArray = sorted(list(t))
        print(tArray)
        for i in range(len(t) - 1):
            gap = tArray[i + 1] - tArray[i]
            if gap > midDay:
                gap = day - gap
            ans = min(ans,gap)
        gap = tArray[-1] - tArray[0]
        if gap > midDay:
            gap = day - gap
        ans = min(ans,gap)
        return ans