import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return d[datetime.datetime(year,month,day).timetuple().tm_wday]