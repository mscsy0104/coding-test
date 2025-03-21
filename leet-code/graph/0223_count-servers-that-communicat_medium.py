'''
https://leetcode.com/problems/count-servers-that-communicate/
'''

from collections import defaultdict
# grid = [[1,0],[0,1]]
# grid = [[1,0],[1,1]]
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

vertex_li = []
for i, row in enumerate(grid):
    for j, col in enumerate(grid[i]):
        if col == 1:
            vertex = 10 * (i+1) + (j+1)
            vertex_li.append(vertex)


graph = dict()
print(graph)
# boundary: grid의 행 길이, grid의 열 길이
for v in vertex_li:
    graph[v] = []
    row_left = v - 10
    row_right = v + 10
    col_left = v - 1
    col_right = v + 1

    min_val = 11
    max_val = len(grid) * 10 + len(grid[0])

    if row_left >= min_val and row_left <= max_val and \
        row_left in vertex_li:
            graph[v].append(row_left)
    if row_right >= min_val and row_right <= max_val and \
        row_right in vertex_li:
            graph[v].append(row_right)
    if col_left >= min_val and col_left <= max_val and \
        col_left in vertex_li:
            graph[v].append(col_left)
    if col_right >= min_val and col_right <= max_val and \
        col_right in vertex_li:
            graph[v].append(col_right)


def recursive_dfs(graph, vertex, visited):
    if vertex not in visited:
        visited.append(vertex)

        for neighbor in graph[vertex]:
            recursive_dfs(graph, neighbor, visited)
    
    return visited

print(graph)

for v in vertex_li:
    visited = []
    print(len(recursive_dfs(graph, v, visited)))
    


