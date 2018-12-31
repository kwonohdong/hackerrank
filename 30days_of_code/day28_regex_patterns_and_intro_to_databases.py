import re

pattern = re.compile(r"[a-z\.]+@gmail\.com")

result = []
for _ in range(int(input())):
    first_name_email_id = input().split()
    first_name = first_name_email_id[0]
    email_id = first_name_email_id[1]
    
    # Solution 1
    m = pattern.match(email_id)

    if m != None:
        result.append(first_name)

    # Solution 2
    # if re.search(r'@gmail\.com$', email_id):
    #     result.append(first_name)

result.sort()
print('\n'.join(result))
