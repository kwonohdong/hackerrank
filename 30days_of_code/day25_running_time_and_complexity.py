import math

def is_prime_number(num:int):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

for _ in range(int(input())):
    n = int(input())
    print(is_prime_number(n))