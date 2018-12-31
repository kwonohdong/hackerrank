from itertools import product
from itertools import permutations

# input()
# a = sorted(map(int, input().split()))
a = sorted(map(int, '12 0 4 3 1 1 12 3 11 11'.split()))
a = sorted(map(int, '1 2 3 4'.split()))

if a[0] == a[-1]:
    print(0)
else:
    k = 31
    while not (((a[0] ^ a[-1]) >> k) & 1):
        k -= 1
# print(min(x ^ y for x, y in product([x for x in a if (x >> k) & 1], [x for x in a if not((x >> k) & 1)])))
print(list(product([x for x in a if (x >> k) & 1], [x for x in a if not((x >> k) & 1)])))


arr = list(permutations('1234'))
result = []
for i in range(len(arr)):
    tmp_result = []

    for j in range(len(arr[i])):
        if j + 1 < len(arr[i]):
            tmp_result.append(int(arr[i][j]) ^ int(arr[i][j+1]))
    
    result.append(max(tmp_result))

# print(result)
# final_result = [max(x) for x in result]
# print(final_result)
# print(min(final_result))
print(min(result))