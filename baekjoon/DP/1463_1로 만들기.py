import sys

input = sys.stdin.readline
n = int(input())

d = [0] * 1000001

def fn(n):
    d[n] = d[n-1] + 1
    if n % 3 == 0:
        d[n] = min(d[n], d[n//3] + 1)
    elif n % 2 == 0:
        d[n] = min(d[n], d[n//2] + 1)

for i in range(2, n+1):
    fn(i)

print(d[n])



'''
1 0
2 1 2/2 
3 1 3/3 
4 2 4/2/2
5 3 5-1/2/2
6 2 6/2/3
7 3 7-1/2/3
8 3 8/2/2/2
9 2 9/3/3
10 3 10-1/3/3
...
'''