# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# top
for i in range(n // 2, 0, -1):
    # left '---------' is 3 times. right '---------' is 3 times. '.|.' is 1, 3, 5, 7 formats odd array.
    print('-'*3*i + '.|.'*(round((m - 6*i) / 3)) + '-'*3*i)

# middle
text = '{:-^' + str(m) + "}"
print(text.format('WELCOME'))

# bottom
for i in range(1, n // 2 + 1):
    # left '---------' is 3 times. right '---------' is 3 times. '.|.' is 1, 3, 5, 7 formats odd array.
    print('-'*3*i + '.|.'*(round((m - 6*i) / 3)) + '-'*3*i)
