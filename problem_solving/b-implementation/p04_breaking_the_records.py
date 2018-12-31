#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    score_tabulate = {'highest_score': scores[0], 'lowest_score': scores[0], 'max': 0, 'min': 0}

    for i in range(1, len(scores)):
        if scores[i] > score_tabulate.get('highest_score'):
            score_tabulate['highest_score'] = scores[i]
            score_tabulate['max'] += 1
        elif scores[i] < score_tabulate.get('lowest_score'):
            score_tabulate['lowest_score'] = scores[i]
            score_tabulate['min'] += 1
    
    return score_tabulate['max'], score_tabulate['min']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
