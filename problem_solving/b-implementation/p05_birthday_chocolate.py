n, s = int(input().strip()), list(map(int, input().split()))
d, m = map(int, input().split())

print(sum([sum(s[i : i + m]) == d for i in range(len(s) - m + 1)]))

# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2

# for i in range(len(s) - m + 1):
#     print(i)
#     print(s[i:i+m], sum(s[i:i+m]) == d)