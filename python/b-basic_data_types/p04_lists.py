if __name__ == '__main__':
    N = int(input())
    result = []

    for _ in range(N):
        method, *args = input().split()

        if method == 'print':
            print(result)
        else:
            getattr(result, method)(*(int(x) for x in args))

