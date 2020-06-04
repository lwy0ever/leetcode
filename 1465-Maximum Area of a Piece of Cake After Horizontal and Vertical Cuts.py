class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        maxH = 0
        for i in range(len(horizontalCuts) - 1):
            maxH = max(maxH,horizontalCuts[i + 1] - horizontalCuts[i])
        maxV = 0
        for i in range(len(verticalCuts) - 1):
            maxV = max(maxV,verticalCuts[i + 1] - verticalCuts[i])
        return maxH * maxV % (10 ** 9 + 7)