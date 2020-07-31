class Solution:
    def reformatDate(self, date: str) -> str:
        import re
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        arr = date.split()
        day = re.findall('\d+',arr[0])[0]
        month = months.index(arr[1]) + 1
        year = arr[2]
        return '-'.join([year,str(month).zfill(2),day.zfill(2)])