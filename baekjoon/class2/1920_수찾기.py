'''
https://www.acmicpc.net/problem/1920
수 찾기

input
5
4 1 5 2 3
5
1 3 7 9 5

output
1
1
0
0
1
'''


# sol1. 이진탐색 이용
import sys

input = sys.stdin.readline

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    return False

input()
arr = sorted(map(int, input().split()))
input()
m_arr = map(int, input().split())

for m in m_arr:
    print(1 if binary_search(arr, m) else 0)


# sol2. hash를 이용한 방법(sol1보다 빠름)
import sys

input = sys.stdin.readline

input()
arr = set(input().split())
input()
m_arr = input().split()

for m in m_arr:
    print(1 if m in arr else 0)