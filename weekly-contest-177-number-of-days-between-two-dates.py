class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        d1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
        d2 = datetime.datetime.strptime(date2,'%Y-%m-%d')
        return abs((d2 - d1).days)