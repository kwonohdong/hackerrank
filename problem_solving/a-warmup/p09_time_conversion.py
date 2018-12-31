#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s.find('PM') > 0:
        hour, minute, second = s.replace('PM', '').split(':')

        if int(hour) < 12:
            hour = str(int(hour) + 12).rjust(2, '0')
        else:
            hour = str(int(hour)).rjust(2, '0')
    else:
        hour, minute, second = s.replace('AM', '').split(':')

        if int(hour) == 12:
            hour = str(0).rjust(2, '0')
        else:
            hour = str(int(hour)).rjust(2, '0')

    return '{}:{}:{}'.format(hour, minute, second)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
