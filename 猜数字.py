class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for i,v in enumerate(guess):
            if v == answer[i]:
                ans += 1
        return ans