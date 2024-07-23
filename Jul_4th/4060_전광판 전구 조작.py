import sys
m, n = map(int, input().split())

bulbs = []
for _ in range(m):
    bulbs.append((sys.stdin.readline().split()))

print(bulbs)
from collections import deque, defaultdict


def bfs(bulbs, root_li):
    visited = []
    queue = deque(root_li)

    while queue:
        vertex = queue.popleft()
        x_idx, y_idx = vertex

        if vertex not in visited:
            visited.append(vertex)


root = (0, 0)
visited = []
stack = [root]

while stack:
    vertex = stack.pop()
    zero_li = one_li = []
    visited = []
    row, col = vertex
    left = row, col-1
    right = row, col+1
    down = row-1, col
    up = row+1, col

    if vertex == 0:
        if left not in visited:
            zero_li.append(left)
            visited.append(left)
        if right not in visited:
            zero_li.append(right)
            visited.append(right)
        if down not in visited:
            zero_li.append(down)
            visited.append(down)
        if up not in visited:
            zero_li.append(up)
            visited.append(up)
    else:
        if left not in visited












# dfs(graph, 4)
