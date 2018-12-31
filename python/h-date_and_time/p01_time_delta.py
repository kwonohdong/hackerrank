from datetime import datetime


# 날짜 및 시간 지정 문자열        의미
# %Y	                        앞의 빈자리를 0으로 채우는 4자리 연도 숫자
# %m	                        앞의 빈자리를 0으로 채우는 2자리 월 숫자
# %d	                        앞의 빈자리를 0으로 채우는 2자리 일 숫자
# %H	                        앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
# %M	                        앞의 빈자리를 0으로 채우는 2자리 분 숫자
# %S	                        앞의 빈자리를 0으로 채우는 2자리 초 숫자
# %A	                        영어로 된 요일 전체 문자열
# %a	                        영어로 된 요일 약어 문자열
# %B	                        영어로 된 월 전체 문자열
# %b	                        영어로 된 월 약어 문자열

fmt = '%a %d %b %Y %H:%M:%S %z'

# a = 'Sun 10 May 2015 13:54:36 -0700'
# b = 'Sun 10 May 2015 13:54:36 -0000'
# print(datetime.strptime(a, fmt))
# print(datetime.strptime(b, fmt))
# print(datetime.strptime(a, fmt) - datetime.strptime(b, fmt))

# a = 'Sat 02 May 2015 19:54:36 +0530'
# b = 'Fri 01 May 2015 13:54:36 -0000'
# print(datetime.strptime(a, fmt))
# print(datetime.strptime(b, fmt))
# print(datetime.strptime(a, fmt) - datetime.strptime(b, fmt))

# a = 'Sat 02 May 2015 19:54:36 +0000'
# b = 'Fri 01 May 2015 13:54:36 -0000'
# print(datetime.strptime(a, fmt))
# print(datetime.strptime(b, fmt))
# print(datetime.strptime(a, fmt) - datetime.strptime(b, fmt))

for i in range(int(input())):
    print(int(abs((datetime.strptime(input(), fmt) - datetime.strptime(input(), fmt)).total_seconds())))