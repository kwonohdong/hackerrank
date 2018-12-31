# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

n, m = map(int, input().split())
arr = [list(map(int, input().split()))[1:] for _ in range(n)]
results = list(map(lambda x: sum(i**2 for i in x) % m, product(*arr)))
print(max(results))

