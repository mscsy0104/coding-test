'''
https://www.acmicpc.net/problem/11866
요세푸스 문제 0

input
7 3

output
<3, 6, 2, 7, 5, 1, 4>
'''


# 틀린 풀이 - IndexError
# 원순열(요세푸스 순열) 고려 필요
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(1, (n+1)))

idx = 0
li = []
while arr:
    if len(arr) > k:
        idx += k - 1
        li.append(arr.pop(idx))

        if idx == len(arr):
            idx = 0
        elif idx == len(arr) - 1:
            idx = -1
    else:
        li.append(arr.pop(idx))

print("<" + ", ".join([str(i) for i in li]) + ">")



# sol1. moduler를 이용한 도로아미타불 기법

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(1, n+1))

idx = 0
result = []

while arr:
    idx = (idx + k - 1) % len(arr)
    result.append(arr.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")



# sol2. deque의 rotate를 이용한 풀이
from collections import deque

n, k = map(int, input().split())
dq = deque(range(1, n + 1))

result = []

while dq:
    dq.rotate(-(k - 1))  # 왼쪽으로 k-1만큼 회전 (앞으로 땡김)
    result.append(dq.popleft())  # k번째 요소 제거

print("<" + ", ".join(map(str, result)) + ">")
