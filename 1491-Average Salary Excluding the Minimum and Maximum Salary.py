class Solution:
    def average(self, salary: List[int]) -> float:
        s = sum(salary)
        mi = min(salary)
        ma = max(salary)
        return (s - mi - ma) / (len(salary) - 2)