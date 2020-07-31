class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if longer == shorter:
            return [longer * k]
        ans = []
        for i in range(k + 1):
            ans.append(longer * i + shorter * (k - i))
        return ans