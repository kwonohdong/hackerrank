n = int(input())
phone_book = {}

for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone

for _ in range(n):
    query = input()
    result = phone_book.get(query)

    if result != None:
        print('{}={}'.format(query, result))
    else:
        print('Not found')