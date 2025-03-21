'''
https://leetcode.com/problems/keys-and-rooms/

'''


def recursive_dfs(graph, ):
    pass



# 리트코드 
rooms = [[2],[],[1]]
# rooms = [[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]
# rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1],[2],[3],[]]

from typing import List

graph = {}
for idx, keys in enumerate(rooms):
    graph[idx] = keys



# dfs 생성
def dfs(graph, start_v, visited):
    stack = [start_v]

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            visited - vertex

            stack.extend(graph[vertex])
    return visited

# dfs 실행
result = dfs(graph, 0)

# 순회 순서와 실제 비교
print(result)



class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 그래프 생성
        graph = {}
        for idx, keys in enumerate(rooms):
            graph[idx] = keys

        # dfs 생성
        def dfs(graph, start_v):
            visited = []
            stack = [start_v]

            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.append(vertex)

                    stack.extend(graph[vertex])
            return visited
        
        # dfs 실행
        result = dfs(graph, 0)

        # 순회 순서와 실제 비교
        print(set(result))
        if result != list(range(len(rooms))):
            return False
        return True
