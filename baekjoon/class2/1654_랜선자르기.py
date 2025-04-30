'''
https://www.acmicpc.net/problem/1654
랜선 자르기

14:36 ~ X
 
input
4 11
802
743
457
539

output
200
'''
import time

start = time.time()
k, n = map(int, input().split())

lanlines = [int(input()) for _ in range(k)]

start = 1
end = max(lanlines)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(line // mid for line in lanlines)

    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)