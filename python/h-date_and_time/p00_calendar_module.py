import calendar
import datetime


# print(calendar.TextCalendar(firstweekday=6).formatyear(2018))
# print(list(calendar.day_name))
# print(datetime.datetime.strptime('08 05 2015', '%m %d %Y').strftime('%A'))

month, day, year = map(int, input().split())

# Solution 1
print(calendar.day_name[calendar.weekday(year, month, day)].upper())

# Solution 2
# print(datetime.datetime.strptime(input(), '%m %d %Y').strftime('%A').upper())