'''
https://www.acmicpc.net/problem/2609
11:19 ~ 11:33

input
24 18

output
6
72
'''
import sys

input = sys.stdin.readline

def gcd(n, m):
    while m > 0:
        n, m = m, n % m

    return n

def lcm(n, m):
    return n * m // gcd(n, m)

n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))

