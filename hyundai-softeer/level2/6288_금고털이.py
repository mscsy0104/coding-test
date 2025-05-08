'''
https://softeer.ai/practice/6288
금고털이

15:17 ~ 16:06

input
100 2
90 1
70 2

output
170
'''

import sys

input = sys.stdin.readline

w, n = map(int, input().split())
price_li = []

for _ in range(n):
    m, p = map(int, input().split())
    price_li.append((m, p))

price_li.sort(key=lambda x:x[1], reverse=True)

result = 0

while w:
    m, p = price_li[idx]
    if w > m:
        result += m * p
        w -= m
        idx += 1
    else:
        result += w * p
        break
    
print(result)


# sol1. while-loop
while w:
    m, p = price_li[idx]
    if w > m:
        result += m * p
        w -= m
        idx += 1
    else:
        result += w * p
        break

# sol2. for-loop
for m, p in price_li:
    if not w:
        break

    if w > m:
        result += m * p
        w -= m
    else:
        result += w * p
        break
    