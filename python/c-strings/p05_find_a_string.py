def count_substring(string, sub_string):
    sub_str_list = []

    for i in range(len(string)):
        num = 0
        sub_text = ''

        for text in string[i:]:
            sub_text += text
            num += 1

            if num == len(sub_string):
                sub_str_list.append(sub_text)
                break
                
    return len(list(filter(lambda a:a == sub_string, sub_str_list)))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)