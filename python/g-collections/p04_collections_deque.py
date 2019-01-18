from collections import deque


n = int(input())
d = deque()

for _ in range(n):
    method, *args = input().split()
    getattr(d, method)(*args)

print(*d)