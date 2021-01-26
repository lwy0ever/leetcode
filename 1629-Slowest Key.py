class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        ans = keysPressed[0]
        longest = releaseTimes[0]
        for i in range(1,n):
            if releaseTimes[i] - releaseTimes[i - 1] >= longest:
                ans = keysPressed[i]
                longest = releaseTimes[i] - releaseTimes[i - 1]
        return ans