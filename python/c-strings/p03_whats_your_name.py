def print_full_name(a, b):
    print("Hello {first_name} {last_name}! You just delved into python.".format(first_name=a[:10], last_name=b[:10]))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)