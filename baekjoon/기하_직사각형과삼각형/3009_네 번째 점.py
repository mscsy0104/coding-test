'''
https://www.acmicpc.net/problem/3009
네 번째 점

input
5 5
5 7
7 5

output
7 7
'''


# sol1. 내 풀이
from collections import Counter

co = [tuple(map(int, input().split())) for _ in range(3)]
x_table = Counter([i[0] for i in co])
y_table = Counter([i[1] for i in co])

print(
    [k for k, v in x_table.items() if v == 1][0], 
    [k for k, v in y_table.items() if v == 1][0]
)


# sol2. 백준 w_h님 풀이
x = [0] * 3
y = [0] * 3

for i in range(3):
    x[i], y[i] = map(int,input().split())

x.sort()
y.sort()

if x[0]==x[1]:
    a = x[2]
else:
    a = x[0]

if y[0]==y[1]:
    b = y[2]
else:
    b = y[0]

print(a,b)


# sol3. 백준 kisukyi31님 풀이
x = [0] * 3
y = [0] * 3
ans_x = 0
ans_y = 0

for i in range(3):
    x[i], y[i] = map(int, input().split())

for i in range(3):
    if x.count(x[i]) < 2:
        ans_x = x[i]
    if y.count(y[i]) < 2:
        ans_y = y[i]

print(ans_x, ans_y)


'''
참고
sol1 확장성 좋음, 현재 입력범위에선 104 ms
sol2, sol3 확장성은 떨어지나 입력범위가 작다면 28ms
'''