'''
https://school.programmers.co.kr/learn/courses/30/lessons/1844


input
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

output 11
'''
from collections import defaultdict
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


graph = defaultdict(list)
# print(graph)
for i, row in enumerate(maps):
    for j, col in enumerate(row):
        if col == 1:
            graph[i+1].append(j+1)
print(graph)