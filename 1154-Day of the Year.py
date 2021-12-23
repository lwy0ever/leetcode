class Solution:
    def dayOfYear(self, date: str) -> int:
        import time
        return time.strptime(date,'%Y-%m-%d').tm_yday