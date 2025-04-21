'''
https://www.acmicpc.net/problem/10816
숫자 카드 2 

16:01 ~ 16:15

input
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

output
3 0 0 1 2 0 0 2
'''

# sol1. collections.Counter 이용
import sys
from collections import Counter

input = sys.stdin.readline

input()
n_counter = Counter(input().split())
input()
m_arr = input().split()

for x in m_arr:
    print(n_counter[x] if x in n_counter.keys() else 0, end=' ')


# sol2. list count 활용 - 시간 초과
input()
n_counter = input().split()
input()
m_arr = input().split()

for x in m_arr:
    print(n_counter.count(x), end=' ')