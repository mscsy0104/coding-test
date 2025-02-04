import sys

sys.stdin = open('input.txt', "r")
t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = int(((x1-x2)**2 + (y1-y2)**2)**(1/2))
    if x1 == x2 and y1 == y2:
        if r1 == r2: print(-1)
        elif abs(r1 - r2) > 0: print(0)
    else: 
        if r  > r1+r2: print(0)
        elif r == r1+r2: print(1)
        elif r < r1+r2 and r > abs(r1-r2): print(2)
        elif r == abs(r1-r2): print(1)
        elif r < abs(r1-r2) and r >= 0: print(0)




