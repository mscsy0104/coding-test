'''
https://softeer.ai/practice/6283
8단 변속기

17:38 ~ 17:44

input
1 2 3 4 5 6 7 8

output
8
'''

# sol1. 분기 처리 이용
import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

cnt = 0
for i in range(len(arr)):
    if arr[i] - 1 == arr[i-1]:
        cnt += 1
    elif arr[i] == arr[i-1] - 1:
        cnt -= 1

if cnt == len(arr) - 1:
    print('ascending')
elif cnt == -1 * (len(arr) - 1):
    print('descending')
else:
    print('mixed')

# sol2. sorted 사용
if arr == sorted(arr):
    print('ascending')
elif arr == sorted(arr, reverse=True):
    print('descending')
else:
    print('mixed')

# 비교
# sol1은 sol2와 비교하면 다소 빠름, 근데 거의 차이 없음.