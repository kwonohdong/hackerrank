from itertools import combinations
import random
import time


def time_checker(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(args, kwargs)
        end_time = time.time()
        print('Executed times:', end_time - start_time)
        return result
    return wrapper

@time_checker
def solution1(a:int, b:list):
    k = a[0]
    ar = a[1]
    
    return sum([1 for x in list(combinations(ar, 2)) if sum(x) % k == 0])

@time_checker
def solution2(a:int, b:list):
    k = a[0]
    ar = a[1]

    count = 0
    for i in range(len(ar)-1):
        for x in range(1+i, len(ar)):
            if (ar[i] + ar[x]) % k == 0:
                count += 1
    
    return count

@time_checker
def solution3(a:int, b:list):
    k = a[0]
    ar = a[1]

    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        # print(f"{ele} {modu} {count} {nums} - after modu")
        count += nums[(k - modu) % k]
        # print(f"{ele} {modu} {count} {nums} - after count+=")
        nums[modu] += 1
        # print(f"{ele} {modu} {count} {nums} - after nums+=")
        # print("-----------------------")
    return count

@time_checker
def solution4(a:int, b:list):
    k = a[0]
    ar = a[1]

    mods = [0] * k
    # print(mods)

    for i in range(len(ar)):
        mods[ar[i] % k] += 1 
        print(mods)

    count = 0
    for i in range(int(k/2) + 1):
        if i == 0:
            count += int(mods[0] * (mods[0] - 1) / 2)
        elif float(i) == (k/2):
            count += int(mods[int(k/2)] * (mods[int(k/2)] - 1) / 2)
        else:
            count += int(mods[i] * mods[k-i])

    return count

n, k = 7, 3
# ar = [random.randint(1, 10) for _ in range(n)]
ar = [1, 3, 2, 6, 4, 5, 9]
print(ar, list(x for x in combinations(ar, 2) if sum(x) % k == 0))

# print(solution1(k, ar)) # O(n^2)
# print(solution2(k, ar)) # O(n^2/2)
# print(solution3(k, ar)) # O(n)
print(solution4(k, ar)) # O(n)

# n, k = map(int, input().split())
# ar = list(map(int, input().split()))
# print(solution4(k, ar))