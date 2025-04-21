'''
https://www.acmicpc.net/problem/10989
수 정렬하기 3

input
10
5
2
3
1
4
2
3
5
1
7

output
1
1
2
2
3
3
4
5
5
7
'''

import sys


# input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)]

# cnt_li = [0] * (max(arr) + 1)

# for i in arr:
#     cnt_li[i] += 1
    
# for i in range(len(cnt_li)):
#     for _ in range(cnt_li[i]):
#         print(i)

input = sys.stdin.readline
n = int(input())
cnt_li = [0] * 10001

for _ in range(n):
    cnt_li[int(input())] += 1

for i in range(10001):
    if cnt_li[i] != 0:
        for _ in range(cnt_li[i]):
            print(i)

# c.f.
# 계수정렬 이해
# https://kill-xxx.tistory.com/entry/python-%EA%B3%84%EC%88%98%EC%A0%95%EB%A0%AC

# 메모리 초과 해결
# https://yoonsang-it.tistory.com/49