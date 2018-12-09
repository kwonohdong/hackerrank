#!/bin/python3

# Constraints: 1 <= n <= 100
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

N = int(input())

# odd number
if N % 2 == 1:
    print('Weird')
# even number
else:
    if N in range(2, 5 + 1):
        print('Not Weird')
    elif N in range(6, 20 + 1):
        print('Weird')
    elif N > 20:
        print('Not Weird')