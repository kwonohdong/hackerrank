import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1, 10 + 1):
        print('{number} x {index} = {result}'.format(number=n, index=i, result=n * i))
