n, p = int(input()), int(input())

# Solution 1
book_pages = []
start_to_end_cnt = 0
end_to_start_cnt = 0

for i in range(1, n + 1, 2):
    if i == 1:
        book_pages.append((None, i))
    else:
        book_pages.append((i - 1, i))

        if i + 1 == n:
            book_pages.append((i + 1, None))

# print(book_pages)

for i in range(len(book_pages)):
    if p in book_pages[i]:
        break
    start_to_end_cnt += 1

for i in range(len(book_pages) - 1, 0, -1):
    if p in book_pages[i]:
        break
    end_to_start_cnt += 1

print(min(start_to_end_cnt, end_to_start_cnt))

# Solution 2
print(min(p//2, n//2-p//2))
