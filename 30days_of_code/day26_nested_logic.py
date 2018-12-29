# Solution 1
actually_returned_date = list(map(int, input().split()))
expected_returned_date = list(map(int, input().split()))

charged = 0

if actually_returned_date[2] > expected_returned_date[2]:
    charged = 10000
elif actually_returned_date[2] == expected_returned_date[2] and actually_returned_date[1] > expected_returned_date[1]:
    charged = 500 * (actually_returned_date[1] - expected_returned_date[1])
elif actually_returned_date[2] == expected_returned_date[2] and actually_returned_date[0] > expected_returned_date[0]:
    charged = 15 * (actually_returned_date[0] - expected_returned_date[0])
else:
    charged = 0

print(charged)

# # Solution 2
# ad, am, ay = map(int, input().split())
# ed, em, ey = map(int, input().split())

# charged = 0

# if ay > ey:
#     charged = 10000
# elif (ay, am) > (ey, em):
#     charged = 500 * (am - em)
# elif (ay, am, ad) > (ey, em, ed):
#     charged = 15 * (ad - ed)
# else:
#     charged = 0

# print(charged)