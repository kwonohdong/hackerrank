n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    string = input().split()
    command = ''
    value = 0

    if (string[0] == 'pop'):
        command = 'pop'
    else:
        command = string[0]
        value = int(string[1])

    if command == 'pop':
        s.pop()
    elif command == 'discard':
        s.discard(value)
    elif command == 'remove':
        s.remove(value)
    else:
        s.pop()

print(sum(s))

