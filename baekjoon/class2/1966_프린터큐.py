'''
https://www.acmicpc.net/problem/1966
프린터 큐

12:21 ~ 13:21

input
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

output
1
2
5
'''
# sol1. max를 이용한 방법
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    imp_queue = deque((i, j) for i, j in enumerate(imp))
    target = imp_queue[m]
    result = []
    
    while imp_queue:
        max_val = max(set(imp))
        first = imp_queue.popleft()
        if first[1] != max_val:
            imp_queue.append(first)
        else:
            result.append(first)
            if first == target:
                break
            imp.remove(first[1])

    print(result.index(target) + 1)



# sol2. 백준 jhhh2222님 풀이
# deque 없이 인덱스로 큐 처리 - 원본 배열 유지 + 확장
t = int(input())

for _ in range(5):
    n, m = map(int, input().split())

    li = list(map(int, input().split()))
    li.sort()

    tu_li = [(i, j) for i, j in enumerate(li)]


    i = 0
    cnt = 0
    while True:
        if tu_li[i][1] == li[i]:
            if tu_li[i][0] == m:
                print(cnt + 1)
                break
            
            cnt += 1
        else:
            tu_li.append(tu_li[i])

            
# queue 쓰는 방법 일부 변형
# sol1. 내가 푼 풀이 - 116 ms
imp = list(map(int, input().split()))
imp_queue = deque((i, j) for i, j in enumerate(imp))
target = imp_queue[m]
result = []

while imp_queue:
    max_val = max(set(imp))
    first = imp_queue.popleft()
    if first[1] != max_val:
        imp_queue.append(first)
    else:
        result.append(first)
        if first == target:
            break
        imp.remove(first[1])


# sol2. any 이용 - 132 ms
queue = deque((i, imp[i]) for i in range(n))

cnt = 0

while queue:
    cur = queue.popleft()
    
    if any(cur[1] < q[1] for q in queue):
        queue.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
