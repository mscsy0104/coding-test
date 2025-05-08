'''
https://softeer.ai/practice/7628
연탄의 크기

17:47 ~ ../ ~ 20:10

input
6
2 4 6 9 12 18

output
5
'''

# 난로 반지름 = k * 연탄 반지름
# 반지름: 정수
# O(n^2) 가능

# sol1. collections.Counter 이용
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

c = 2
counter = Counter()

while c <= max(arr):
    cnt = 0

    for i in arr:
        if i % c == 0:
            cnt += 1

    counter[c] = cnt

    c += 1
    
print(counter.most_common(1)[0][1])


# sol2. 누적합, 최대 횟수 이용
max_cnt = 0

for c in range(2, max(arr) + 1):
    cnt = sum(1 for r in arr if r % c == 0)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)