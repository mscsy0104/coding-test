'''
https://www.acmicpc.net/problem/2738
행렬 덧셈

15:47 ~ 16:05

input
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

output
4 4 4
6 6 6
5 6 100
'''
 
# sol1. memory 111008KB, time 104ms
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

def add_matix_elements(n, m, matrix1, matrix2):
    matrix = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix

matrix = add_matix_elements(n, m, a, b)
for arr in matrix:
    print(*arr)


# sol2. memory 111028KB, time 104ms
'''코드 길이는 짧지만, 매 줄마다 리스트를 새로 만들고 즉시 출력하는 구조라서

잠깐 동안이더라도 중간 리스트(result_row)가 계속 메모리를 점유하게 돼

반면, sol1 코드는 한 번만 리스트를 만들고 나중에 출력하니까 메모리는 조금 덜 사용'''
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    row = [a[i][j] + b[i][j] for j in range(m)]
    print(*row)
