'''
https://www.acmicpc.net/problem/11651
좌표 정렬하기 2

input
5
0 4
1 2
1 -1
2 2
3 3

output
1 -1
1 2
2 2
3 3
0 4
'''

import sys
from operator import itemgetter

input = sys.stdin.readline
n = int(input())
li = []

for _ in range(n):
    li.append(tuple(map(int, input().split())))

li.sort(key=itemgetter(1, 0))

for i in li:
    print(*i)

'''
sol1.
li.sort(key=lambda x:(x[1], x[0]))

sol2.
from operator import itemgetter

li.sort(key=itemgetter(1, 0))

sol1과 sol2의 차이
sol2가 C 기반이라 다소 빠름.
입력값이 아주 크지 않으면 큰 차이는 나지 않지만 참고.
'''
