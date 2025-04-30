'''
https://www.acmicpc.net/problem/18110
solved.ac

17:03 ~ 17:23

input
5
1
5
5
7
8

output
6
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n:
    arr.sort()
    round_avg = int(n * 0.15 + 0.5)
    arr = arr[round_avg:len(arr) - round_avg]

    print(int(sum(arr)/len(arr) + 0.5))
else:
    print(0)