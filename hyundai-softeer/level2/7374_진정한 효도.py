'''
https://softeer.ai/practice/7374
진정한 효도

16:41 ~ 17:22

input
1 1 1
2 3 1
3 1 2

output
0
'''
# sol1. collections.Counter 이용
from collections import Counter
import sys
import time

start = time.time()

input = sys.stdin.readline

def check_price(bar):
    counter = Counter(bar)
    len_val = len(counter)

    if len_val == 1:
        return 0
    elif len_val == 2:
        c = counter.most_common(2)
        return abs(c[1][0] - c[0][0])
    else:
        return 2
    

ground = []
for _ in range(3):
    ground.append(list(map(int, input().split())))


price_li = []
for i in range(3):
    price_li.append(check_price(ground[i]))

    col = []
    for j in range(3):
        col.append(ground[j][i])

    price_li.append(check_price(col))

print(min(price_li))

        
# sol2-1. 
ground = [list(map(int, input().split())) for _ in range(3)]

min_cost = float('inf')

for row in ground:
    for target_height in range(1, 4):
        cost = sum(abs(cell - target_height) for cell in row)
        min_cost = min(min_cost, cost)

for c_idx in range(3):
    col = [ground[r_idx][c_idx] for r_idx in range(3)] 
    for target_height in range(1, 4): 
        cost = sum(abs(cell - target_height) for cell in col)
        min_cost = min(min_cost, cost)

print(min_cost)



# sol2-2.
ground = [list(map(int, input().split())) for _ in range(3)]

def get_min_cost(bar):
    return min(sum(abs(cell - h) for cell in bar) for h in range(1, 4))

for row in ground:
    min_cost = min(min_cost, get_min_cost(row))

for c_idx in range(3):
    col = [ground[r_idx][c_idx] for r_idx in range(3)] 
    min_cost = min(min_cost, get_min_cost(col))


print(min(price_li))

# sol1 v.s. sol2
# sol1: 3.87s
# sol2: 2.37s