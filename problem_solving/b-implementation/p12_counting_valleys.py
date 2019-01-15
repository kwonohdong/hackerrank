n = int(input())
s = input()

result = 0
position = 0
for i in range(n):        
    if s[i] == 'U':
        position += 1
    else:
        position += -1
        
    if position == 0 and s[i] == 'U':
        result += 1
        
print(result)
