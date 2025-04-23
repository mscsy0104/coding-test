'''
https://www.acmicpc.net/problem/11050
이항 계수 1

11:10 ~ 11:16

input
5 2

output
10
'''
import sys

input = sys.stdin.readline
n, k = map(int, input().split())

x = 1
for i in range(n, n - k, -1):
    x *= i

d = 1
for i in range(1, k+1):
    d *= i

print(x//d)