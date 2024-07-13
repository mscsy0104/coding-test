n = int(input())
x, y = map(int, input().split())

rows = cols = n
graph = [[0 for _ in range(cols)] for _ in range(rows)]

graph[x-1][y-1] = 1

def bfs(graph, x, y):
    visited = []
    queue = [[x-1, y-1]]
    # queue = deque([x-1, y-1])

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            x_idx, y_idx = vertex[0], vertex[1]
            increased_value = graph[x_idx][y_idx] + 1
            if x_idx - 1 >= 0 and graph[x_idx-1][y_idx] == 0:
                graph[x_idx-1][y_idx] += increased_value
                queue.append([x_idx-1, y_idx])
            if x_idx + 1 < n and graph[x_idx+1][y_idx] == 0:
                graph[x_idx + 1][y_idx] += increased_value
                queue.append([x_idx + 1, y_idx])
            if y_idx - 1 >= 0 and graph[x_idx][y_idx-1] == 0:
                graph[x_idx][y_idx - 1] += increased_value
                queue.append([x_idx, y_idx - 1])
            if y_idx + 1 < n and graph[x_idx][y_idx+1] == 0:
                graph[x_idx][y_idx + 1] += increased_value
                queue.append([x_idx, y_idx + 1])

    return graph

result = bfs(graph, x, y)

for rows in result:
    for cols in rows:
        print(cols, end=' ')
    print()
