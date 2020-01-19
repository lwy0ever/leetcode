class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        return self.superPow(a,b) ** 10 % 1337 * (a ** last) % 1337