if __name__ == '__main__':
    s = input()

    # Solution 1
    # print(any(text.isalnum() for text in s))
    # print(any(text.isalpha() for text in s))
    # print(any(text.isdigit() for text in s))
    # print(any(text.islower() for text in s))
    # print(any(text.isupper() for text in s))

    # Solution 2
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(text) for text in s))
        
