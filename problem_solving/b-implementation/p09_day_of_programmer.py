year = int(input().strip())

if year == 1918:
    print('26.09.{}'.format(year))
# leap year
elif year % 4 == 0 and (year < 1918 or year % 400 == 0 or year % 100 != 0):
    print('12.09.{}'.format(year))
else:
    print('13.09.{}'.format(year))

