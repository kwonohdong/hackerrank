n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())

# n, k = 4, 1
# bill = [3, 10, 2, 9]
# b = 12

print('Bon Appetit' if (sum(bill) - bill[k]) // 2 == b else bill[k] // 2)