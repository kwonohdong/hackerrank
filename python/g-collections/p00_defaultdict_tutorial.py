from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

m_result = []

for i in range(n):
    x = input()
    d[x].append(i+1)

for i in range(m):
    m_result.append(input())

for x in m_result:
    if x in d:
        print(" ".join(map(str, d[x])))
    else:
        print(-1)