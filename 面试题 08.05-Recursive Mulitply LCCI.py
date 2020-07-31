class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A > B:
            A,B = B,A
        # A <= B
        ans = 0
        while A:
            if A & 1:
                ans += B
            A >>= 1
            B <<= 1
        return ans