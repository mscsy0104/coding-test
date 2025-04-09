'''
https://www.acmicpc.net/problem/2231
분해합

23:30 ~ 23:46

input
216

output
198
'''

n = int(input())

generators = []
for i in range(1, n):
    total = 0
    units = [int(j) for j in str(i)]

    total = i + sum(units)

    if total == n:
        generators.append(i)

if generators:
    print(min(generators))
else:
    print(0)