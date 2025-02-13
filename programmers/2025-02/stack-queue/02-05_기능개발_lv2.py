'''
12:10 ~ 
https://school.programmers.co.kr/learn/courses/30/lessons/42586

input: 
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

output:
[1, 3, 2]
'''

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    remains = deque()
    for p, s in zip(progresses, speeds):
        remain = math.ceil((100 - p) / s)
        remains.append(remain)

    while remains:
        count = 0
        if remains:
            current = remains.popleft()
            count += 1

        while remains and remains[0] <= current:
            remains.popleft()
            count += 1

        answer.append(count)

    return answer