if __name__ == '__main__':
    N = int(input())

    # if N % 2 == 1:
    #     print("Weird")
    # elif N % 2 == 0:
    #     if N in range(2, 6):
    #         print("Not Weird")
    #     elif N in range(6, 20 + 1):
    #         print("Weird")
    #     elif N > 20:
    #         print("Not Weird")
    
    if N % 2 == 1 or (N > 5 and N < 21):
        print("Weird")
    else:
        print("Not Weird")
