#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort(reverse=True)
    max_list = [arr[i] for i in range(len(arr)-1)]

    arr.sort()
    min_list = [arr[i] for i in range(len(arr)-1)]
    return print(sum(min_list), sum(max_list))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)