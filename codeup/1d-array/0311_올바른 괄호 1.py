'''
https://codeup.kr/problem.php?id=1410
1410 : 올바른 괄호 1

input
((())()(()))

output
6 6
'''
import time

start1 = time.time()
gwalho = list(input())

left_cnt = 0
right_cnt = 0
for i in gwalho:
    if i == '(':
        left_cnt += 1
    elif i == ')':
        right_cnt += 1

print(left_cnt, right_cnt)
end1 = time.time()


start2 = time.time()
from collections import Counter

counter = Counter(gwalho)
# print(counter.items())
sorted_counter = sorted(counter.items(), key=lambda x: x[0] != '(')
# print(sorted_counter)

print(sorted_counter[0][1], sorted_counter[1][1])
end2 = time.time()


notice = f'''
time1: {end1 - start1}
time2: {end2 - start2}
'''
print(notice)

'''
time1: 1.725877046585083
time2: 0.00019502639770507812
'''