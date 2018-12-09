if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(' ')))

    new_arr = [item for item in arr if item != max(arr)]
    print(max(new_arr))

