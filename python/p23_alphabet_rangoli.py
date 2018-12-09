import string

def print_rangoli(size):
    # size 1, each line 0 * 2 + 1 = 1
    # size 2, each line 2 * 2 + 1 = 5
    # size 3, each line 4 * 2 + 1 = 9
    # size 4, each line 6 * 2 + 1 = 13
    # size 5, each line 8 * 2 + 1 = 17
    # size 6, each line 10 * 2 + 1 = 21

    # your code goes here
    alpha = string.ascii_lowercase
    result = []

    for i in range(size):
        text = '-'.join(alpha[i:size])
        result.append((text[::-1] + text[1:]).center(4*size-3, '-'))

    print('\n'.join(result[:0:-1] + result))

