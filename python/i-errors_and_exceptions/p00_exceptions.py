t = int(input())

for _ in range(t):
    try:
        a, b = input().split()

        print(int(int(a) // int(b)))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except Exception as e:
        print("Error Code:", e)
    except BaseException as e:
        print("Error Code:", e)