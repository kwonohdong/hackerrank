from collections import namedtuple


n = int(input())
fields_name = input()
StudentInfo = namedtuple('StudentInfo', fields_name, rename=True)
score_list = [int(StudentInfo._make(input().split()).MARKS) for _ in range(n)]

print('{0:.2f}'.format(sum(score_list) / len(score_list)))
