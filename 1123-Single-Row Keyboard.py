class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = 0
        pre = 0
        for c in word:
            np = keyboard.index(c)
            ans += abs(np - pre)
            pre = np
        return ans