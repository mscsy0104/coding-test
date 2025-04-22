'''
https://www.acmicpc.net/problem/10845
큐

10:38 ~ 10:51

input
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

output
1
2
2
0
1
2
-1
0
1
-1
0
3
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    comm = input().strip()

    splitted_comm = comm.split()
    if splitted_comm[0] == 'push':
        queue.append(splitted_comm[1])
    elif comm == 'pop':
        print(queue.popleft() if queue else -1)
    elif comm == "size":
        print(len(queue))
    elif comm == "empty":
        print(0 if queue else 1)
    elif comm == "front":
        print(queue[0] if queue else -1)
    elif comm == "back":
        print(queue[-1] if queue else -1)