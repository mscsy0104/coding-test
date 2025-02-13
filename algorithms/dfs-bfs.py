def iterative_bfs(graph, start_v):
    visited = [start_v]
    queue = start_v
    
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


def iterative_dfs(graph, start_v):
    visited = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)

    return visited


def recursive_dfs(graph, visited, v):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = recursive_dfs(graph, visited, v)
    return visited