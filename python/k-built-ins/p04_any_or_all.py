# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
ar = list(map(int, input().split()))

print(all(i > 0 for i in ar) and any(str(i) == str(i)[::-1] for i in ar))

