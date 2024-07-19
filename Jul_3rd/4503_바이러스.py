from collections import deque
import sys
from collections import defaultdict

def bfs(graph, root):
    visited = []
    queue = deque(root)

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]) - set(visited))
    return visited

def make_graph(arr):
    key_list = []
    for coulple in arr:
        key_list.append(coulple[0])

    lod = defaultdict(list)
    for couple in arr:
        lod[couple[0]].append(couple[1])
        lod[couple[1]].append(couple[0])
    return lod



arr = []
with open('input.txt', 'r') as file:
    for i in file:
        arr.append(i.split())

n = int(arr[0][0])
t = int(arr[1][0])
array = arr[2:]
graph = make_graph(array)

# n = int(input())
# t = int(input())
# arr = [list(input().split()) for _ in range(t)]
# graph = make_graph(arr)

path = bfs(graph, '1')


print(len(path)-1)