class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        m = [0] * (n + 1)
        for i,j,k in bookings:
            m[i - 1] += k
            m[j] -= k
        ans = []
        c = 0
        for i in range(n):
            c += m[i]
            ans.append(c)
        return ans