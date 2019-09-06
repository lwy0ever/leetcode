import bisect
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n == 1:
            return 0
        sticks.sort()
        i = 0
        ans = 0
        while i < n + n - 2:
            ns = sticks[i] + sticks[i + 1]
            ans += ns
            bisect.insort_left(sticks,ns)
            i += 2
            #print(sticks,i)
        return ans