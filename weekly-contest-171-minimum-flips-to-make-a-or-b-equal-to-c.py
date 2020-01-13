class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a > 0 or b > 0 or c > 0:
            #print(bin(a),bin(b),bin(c))
            if c & 1 == 0:
                ans += (a & 1) + (b & 1)
            else:
                ans += not ((a | b) & 1)
            a >>= 1
            b >>= 1
            c >>= 1
            #print(ans)
        return ans