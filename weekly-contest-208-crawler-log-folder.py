class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for op in logs:
            match op:
                case '../':
                    ans = ans - 1 if ans > 0 else 0
                case './':
                    continue
                case _:
                    ans += 1
        return ans