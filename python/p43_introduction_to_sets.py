def average(array):
    # your code goes here
    distinct_arry = set(array)
    return sum(distinct_arry) / len(distinct_arry)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)