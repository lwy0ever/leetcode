class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = collections.Counter(moves)
        return cnt['L'] == cnt['R'] and cnt['U'] == cnt['D']