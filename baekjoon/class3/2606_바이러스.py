'''
https://www.acmicpc.net/problem/2606
바이러스

17:30 ~ 18:00

input
7
6
1 2
2 3
1 5
5 2
5 6
4 7

output
4
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
p = int(input())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# cnt가 중요하니까 visited를 set로 처리해도 됨.(add)
# 순서를 알고싶을 땐 visited를 배열로 처리.(append)
# sol1. bfs
def bfs(graph, start_v):
    queue = deque([start_v])
    # visited = []
    visited = set()

    while queue:
        curr_v = queue.popleft()

        if curr_v not in visited:
            # visited.append(curr_v)
            visited.add(curr_v)
            for neighbor in graph[curr_v]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return visited


print(len(bfs(graph, 1)) - 1)


# sol2. dfs
def dfs(graph, start_v):
    stack = deque([start_v])
    # visited = []
    visited = set()

    while stack:
        curr_v = stack.pop()

        if curr_v not in visited:
            # visited.append(curr_v)
            visited.add(curr_v)
            for neighbor in graph[curr_v]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


print(len(dfs(graph, 1)) - 1)


# 배열 순서가 궁금할 때는 visited = []하고 아래 확인
print(len(bfs(graph, 1)) - 1)
print(bfs(graph, 1))
print(len(dfs(graph, 1)) - 1)
print(dfs(graph,1))
