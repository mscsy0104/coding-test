'''
https://www.acmicpc.net/problem/2164
카드2

input 
6

output
4
'''

import time
import sys
from collections import deque

start = time.time()

input = sys.stdin.readline
n = int(input())
arr = deque(range(1, n + 1))

while len(arr) > 1:
    arr.popleft()
    temp = arr.popleft()
    arr.append(temp)

print(arr[0])

print(time.time() - start)