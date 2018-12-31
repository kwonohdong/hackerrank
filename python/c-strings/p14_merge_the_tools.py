def merge_the_tools(string, k):
    # Repeat the string 'S' by k.
    for i in range(0, len(string), k):
        slice_str = string[i:i+k]
        uni_arr = []

        for x in slice_str:
            if x not in uni_arr:
                uni_arr.append(x)
        print(''.join(uni_arr))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)