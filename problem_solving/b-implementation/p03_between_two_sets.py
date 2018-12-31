from functools import reduce
from math import gcd


input()
a = map(int,input().strip().split())
b = map(int,input().strip().split())
# a = [2, 4] # 4, 8, 16, 32
# b = [16, 32, 96] # 4, 8, 16

lcm_a = reduce(lambda x,y: x*y//gcd(x, y), a)
gcd_b = reduce(gcd, b)

print(lcm_a, gcd_b)
print(sum(1 for x in range(lcm_a, gcd_b+1, lcm_a) if gcd_b % x == 0))