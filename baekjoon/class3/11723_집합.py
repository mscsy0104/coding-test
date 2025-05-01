'''
https://www.acmicpc.net/problem/11723
집합

13:46 ~ 14:01

input
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

output
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''
# sol1. set 메소드 쓴 방법
import sys

input = sys.stdin.readline

m = int(input())
s = set()
result = []

for _ in range(m):
    comm = input().strip()

    if comm == 'all':
        s = {str(i) for i in range(1, 21)}
    elif comm == 'empty':
        s.clear()
    else:
        comm, x = comm.split()
        if comm == 'add':
            if x not in s:
                s.add(x)
        elif comm == 'remove':
            if x in s:
                s.remove(x)
        elif comm == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif comm == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)


# sol2. 백준 rnxogud136님 풀이
# 우아해서 놀랐다..!
import sys

read = sys.stdin.readline
write = sys.stdout.write

table = [False] * 21

m = int(read())

for _ in range(m):
    comm = read().split()
    num = 0

    if len(comm) > 1:
        num = int(comm[1])
    
    if comm[0] == 'add':
        table[num] = True
    elif comm[0] == 'remove':
        table[num] == False
    elif comm[0] == 'check':
        write(str(1 if table[num] else 0) + '\n')
    elif comm[0] == 'toggle':
        table[num] = not table[num]
    elif comm[0] == 'all':
        table = [True] * 21
    elif comm[0] == 'empty':
        table = [False] * 21
    