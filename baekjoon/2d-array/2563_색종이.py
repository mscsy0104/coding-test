'''
https://www.acmicpc.net/problem/2563
색종이

18:19 ~ X(해설)

input
3
3 7
15 7
5 2

output
260
'''




# sol1. (틀린 풀이): 점으로 생각
'''
주어진 값 -> 행렬 만들기
3 7

x: 3 ~ 13
y: 7 ~ 17

square = [[0 * 100] for _ in range(100)]

for i in range(3, 13 + 1):
    for j in range(7, 17 + 1):
        square[i][j] = 1

for i in square:
    print(i)
# '''
# n = int(input())
# square = [[0]*n for _ in range(n)]

# for i in square:
#     print(*i)
# def paint_black_rectangle(x, y):
#     for col in range(x, x + 11):
#         for row in range(y,  + 11):
#     # for col in range(3, 13 + 1):
#     #     for row in range(7, 17 + 1):
#             if square[row][col] == 0:
#                 square[row][col] = 1
#             else:
#                 square[row][col] = 2

# paint_black_rectangle(3, 7)

# paint_black_rectangle(15, 7)

# paint_black_rectangle(5, 2)


# total = 0
# for i in square:
#     total += sum(i)

# print(total) # 243


# sol2. (옳은 풀이): 칸으로 생각
paper = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# (sum(row) for row in paper) # <generator object <genexpr> at 0x104a86a80>
black_area = sum(sum(row) for row in paper) # row 별로 더하고, 그걸 또 더한다.
print(black_area)


# 잘한 점: 좌표와 요소를 도형 개념으로 생각
# 아쉬운 점: 칸인지 점인지 구분 못 함.