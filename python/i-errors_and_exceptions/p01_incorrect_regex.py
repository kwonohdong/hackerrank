import re


for _ in range(int(input())):
    try:
        pattern = re.compile(input())
        print(True)
    except re.error as e:
        print(False)