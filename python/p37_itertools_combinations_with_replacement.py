from itertools import combinations_with_replacement


s, k = input().split()
print(*[''.join(x) for x in combinations_with_replacement(sorted(s), int(k))], sep='\n')