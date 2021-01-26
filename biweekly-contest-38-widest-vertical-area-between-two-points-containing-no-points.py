class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        pre = float('inf')
        for x,_ in sorted(points,key = lambda x:x[0]):
            ans = max(ans,x - pre)
            pre = x
        return ans