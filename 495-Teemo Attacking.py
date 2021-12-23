class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        mx = 0
        for t in timeSeries:
            ans += duration if t > mx else t - mx + duration
            mx = t + duration
            #print(t,mx,ans)
        return ans
