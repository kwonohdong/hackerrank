arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))
count = [0] * 6

for t in arr:
    count[t] += 1

print(count.index(max(count)))