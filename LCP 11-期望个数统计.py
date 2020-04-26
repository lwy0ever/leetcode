class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        # 假设某一个值,有n个相同的数字,则每个值有1/n的可能性相同,也就是n * 1/n = 1
        return len(set(scores))