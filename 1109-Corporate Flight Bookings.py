class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0] * (n + 2)
        for f,l,s in bookings:
            pre[f] += s
            pre[l + 1] -= s
        #print(pre)
        ans = [0] * n
        cnt = 0
        for i in range(n):
            cnt += pre[i + 1]
            ans[i]  = cnt
        return ans