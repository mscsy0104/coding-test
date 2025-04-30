'''
https://www.acmicpc.net/problem/10773
제로

17:45 ~ 17:52

input
4
3
0
4
0

output
0
'''
from collections import deque
import sys

input = sys.stdin.readline

k = int(input())

nums = [int(input()) for _ in range(k)]
result = deque()

for i in nums:
    if i:
        result.append(i)
    else:
        result.pop()

print(sum(result))