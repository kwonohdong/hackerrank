#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

# n = 5
# a = [3, 2, 1]
# a = [1, 2, 3, 4, 5]

def bubble_sort(arr:list) -> int:
    swap_cnt = 0

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swap_cnt += 1
        
        if swap_cnt == 0:
            break
    return swap_cnt

print('Array is sorted in {swap_cnt} swaps.'.format(swap_cnt=bubble_sort(a)))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
