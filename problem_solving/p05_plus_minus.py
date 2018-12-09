#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_ratio = '{:.6f}'.format(sum([1 for item in arr if item > 0]) / len(arr))
    negative_ratio = '{:.6f}'.format(sum([1 for item in arr if item < 0]) / len(arr))
    zero_ratio = '{:.6f}'.format(sum([1 for item in arr if item == 0]) / len(arr))
    print('\n'.join([positive_ratio, negative_ratio, zero_ratio]))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
