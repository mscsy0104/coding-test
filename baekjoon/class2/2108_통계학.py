'''
https://www.acmicpc.net/problem/2108
통계학
11:16 ~ 11:57

input
5
1
3
8
-2
2

output
2
2
1
10
'''
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 1. 산술평균(반올림)
print(round(sum(nums) / n))

# 2. 중앙값
nums.sort()
print(nums[len(nums)//2])

# 3. 최빈값
counter = Counter(nums)
max_val = max(counter.values())

li = [k for k, v in counter.items() if v == max_val]

li.sort()

print(li[1] if len(li) > 1 else li[0])

# 4. 범위
print(max(nums) - min(nums))
