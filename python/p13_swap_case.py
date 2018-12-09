def swap_case(s):
    result = ''

    for text in s:
        if text.isupper():
            result += text.lower()
        else:
            result += text.upper()

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)