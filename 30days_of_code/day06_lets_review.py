# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    # Solution 1
    # user_string = input()
    # even_result = ''
    # odd_result = ''
    # for i in range(len(user_string)):
    #     if i % 2 == 0:
    #         even_result += user_string[i]
    #     else:
    #         odd_result += user_string[i]
            
    # print(even_result, odd_result)

    # Solution 2
    user_string = input()
    print(user_string[::2], user_string[1::2])
