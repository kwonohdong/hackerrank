# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
shoe_size = list(map(int, input().split()))
n = int(input())
# x = 10
# shoe_size = list(map(int, '2 3 4 5 6 8 7 6 5 18'.split()))
# n = 6

shoe_size_dict = Counter(shoe_size)
result = 0
for _ in range(n):
    s, p = map(int, input().split())
    
    if shoe_size_dict.get(s) != None:
        shoe_size_dict[s] -= 1
        result += p

        if shoe_size_dict[s] == 0:
            del(shoe_size_dict[s])
    else:
        continue

print(result)
