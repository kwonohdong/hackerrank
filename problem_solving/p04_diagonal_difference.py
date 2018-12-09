#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    first_diagonal = 0
    second_diagonal = 0

    # arr[0][0] + arr[1][1] + arr[2][2]
    # arr[0][2] + arr[1][1] + arr[2][0]
    
    # arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3]
    # arr[0][3] + arr[1][2] + arr[2][1] + arr[3][0]

    for i in range(len(arr)):
        first_diagonal += arr[i][i]
        second_diagonal += arr[i][len(arr)-1 - i]

    return abs(first_diagonal - second_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
