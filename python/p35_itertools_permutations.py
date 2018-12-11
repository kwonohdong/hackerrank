# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


s, k = input().split()

# Solution 1
# result = list(permutations(s, int(k)))
# result.sort()

# for x in result:
#     print(*x, sep='')

# Solution 2
# Permutations function result are (A,C), (A,H), (A,K) ... (K,H), that elements of result is tuple.
# It combines the elements of the tuple and unpacks the result, and print the result again.
print(*[''.join(x) for x in permutations(sorted(s), int(k))], sep='\n')