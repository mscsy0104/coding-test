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