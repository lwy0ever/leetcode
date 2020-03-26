class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0
        # 由于n <= 10 ^ 9
        # 而同时 reservedSeats.length <= min(10*n, 10^4)
        # 可见reservedSeats的数量相对较小
        seats = {r:0 for r,c in reservedSeats}
        #print(len(seats))
        #return 0
        for r,c in reservedSeats:
            seats[r] |= 1 << (c - 1)
        ans += (n - len(seats)) * 2 # 一个空行,可以容纳2个家庭
        for seat in seats.values():
            for j in [1,3,5]:   # 4人连座,则起始位置应该是2,4,6,对应base0的起点为1,3,5
                for x in range(4):
                    if seat & (1 << (j + x)):
                        break
                    else:
                        seat |= 1 << (j + x)
                else:
                    ans += 1
        return ans