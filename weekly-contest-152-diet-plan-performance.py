class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        n = len(calories)
        if n < k:
            return 0
        s = sum(calories[:k])
        if s < lower:
            score -= 1
        if s > upper:
            score += 1
        for i in range(1,n - k + 1):
            s -= calories[i - 1]
            s += calories[i + k - 1]
            if s < lower:
                score -= 1
            if s > upper:
                score += 1
        return score