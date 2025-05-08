'''
https://softeer.ai/practice/9657
나무 공격

16:15 ~ 16:31

input
6 8
0 0 1 0 0 0 1 0
0 0 0 1 0 0 0 0
0 0 1 0 0 1 1 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
1 5
2 6

output
2
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(sum(list(map(int, input().split()))))

l1, r1 = map(int, input().split())
l2, r2 = map(int, input().split())


for i in range(l1 - 1, r1):
    if graph[i] > 0:
        graph[i] -= 1


for i in range(l2 - 1, r2):
    if graph[i] > 0:
        graph[i] -= 1


print(sum(graph))


        