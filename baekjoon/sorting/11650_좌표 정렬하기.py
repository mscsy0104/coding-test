'''
https://www.acmicpc.net/problem/11650
좌표 정렬하기

input
5
3 4
1 1
1 -1
2 2
3 3

output
1 -1
1 1
2 2
3 3
3 4
'''


import sys

input = sys.stdin.readline
n = int(input())
li = []

for _ in range(n):
    li.append(tuple(map(int, input().split())))

li.sort(key=lambda li: (li[0], li[1]))

for i in li:
    print(*i)