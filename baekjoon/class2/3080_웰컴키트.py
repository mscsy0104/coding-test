'''
https://www.acmicpc.net/problem/30802
웰컴 키트
1:12 ~ 1:20

input
23
3 1 4 1 5 9
5 7

output
7
3 2
'''

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0 
for i in arr:
    if i % t == 0:
        cnt += (i // t)
    else:
        cnt += (i // t + 1)
    
print(cnt)
print(*divmod(n, p))



# cnt 계산 비교
# sol1. for loop 기본 방법
cnt = 0 
for i in arr:
    if i % t == 0:
        cnt += (i // t)
    else:
        cnt += (i // t + 1)

# sol2. for-loop + pythonic한 방법
cnt = 0 
for i in arr:
    cnt += i // t + (1 if i % t != 0 else 0)

# sol3. map, lambda 이용 + pythonic한 방법
cnt = sum(map(lambda x: x // t + (1 if x % t != 0 else 0), arr))