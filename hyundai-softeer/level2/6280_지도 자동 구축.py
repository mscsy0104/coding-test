'''
https://softeer.ai/practice/6280
지도 자동 구축

17:26 ~ 17:35

input
1

output
9
'''
# 2, 3=2+1, 5=3+2, 9=5+4, 19=10+9, ...
# 1, 2,     3,     4,    5
import sys

input = sys.stdin.readline

n = int(input())
cnt = 2

for i in range(1, n + 1):
    cnt += cnt - 1

print(cnt ** 2)
    