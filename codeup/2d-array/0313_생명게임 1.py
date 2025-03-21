'''
https://codeup.kr/problem.php?id=1515
1515 : 생명 게임 1

출력할때 각 행의 마지막 25열의 정보(1또는 0)를 출력 후 반드시 공백을 출력해야 합니다.(표현오류때문)

input
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 1 0 1 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 1 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 0 
0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 

output
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
'''



'''
1. 고정
2. 
반복문으로 돌면서
0인 요소에 대해서, 주위 8칸을 확인하는 함수를 작성한다.
주위 8칸에 3개가 1이면 해당 요소를 1로 바꿔준다.
1인 요소에 대해서, 주위 8칸을 확인하는데,(위에서 만든 함수로)
주위 4칸 이상 혹은 1칸 이하 1인 경우, 해당요소를 0으로 바꿔준다.
1인 요소에 대해서, 주위 8칸을 확인하는데
주위 2 ~ 3칸에 1이 있으면, 1로 그대로 둔다.


3. On^2
'''
matrix = [list(map(int, input.split())) for _ in range(25)] # 개선: list comprehension 
# matrix = []
# for _ in range(25):
#     row = list(map(int, input().split()))
#     matrix.append(row)


def check_neighbor(r_idx, c_idx, matrix):
    cnt = 0
    majinot = len(matrix[0]) - 1
    if r_idx - 1 >= 0 and c_idx - 1 >= 0 and matrix[r_idx - 1][c_idx - 1] == 1:
        cnt += 1
    if r_idx - 1 >= 0 and matrix[r_idx - 1][c_idx] == 1:
        cnt += 1
    if r_idx - 1 >= 0 and c_idx + 1 <= majinot and matrix[r_idx - 1][c_idx + 1] == 1:
        cnt += 1
    if c_idx - 1 >= 0 and matrix[r_idx][c_idx - 1] == 1:
        cnt += 1
    if c_idx + 1 <= majinot and matrix[r_idx][c_idx + 1] == 1:
        cnt += 1
    if r_idx + 1 <= majinot and c_idx - 1 >= 0 and matrix[r_idx + 1][c_idx - 1] == 1:
        cnt += 1
    if r_idx + 1 <= majinot and matrix[r_idx + 1][c_idx] == 1:
        cnt += 1
    if r_idx + 1 <= majinot and c_idx + 1 <= majinot and matrix[r_idx + 1][c_idx + 1] == 1:
            cnt += 1

    return cnt


new_generation = [[0]*25 for _ in range(25)]
for r_idx, row in enumerate(matrix):
    for c_idx, col in enumerate(row):
        cnt = check_neighbor(r_idx, c_idx, matrix)
        if col == 0 and cnt == 3:
            new_generation[r_idx][c_idx] = 1
        elif col == 1 and cnt >= 4 or cnt <= 1:
            new_generation[r_idx][c_idx] = 0
        elif col == 1 and cnt == 2 or cnt == 3:
            new_generation[r_idx][c_idx] = 1

for row in new_generation:
    print(*row)



'''
c.f. GPT 추천 
def check_neighbor(r_idx, c_idx, matrix):
    cnt = 0 
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        nr, nc = r_idx + dr, c_idx + dc
        if 0 <= nr < 25 and 0 <= nc < 25 and matrix[nr][nc] == 1:
            cnt += 1

    return cnt

new_generation = [[0]*25 for _ in range(25)]
for r_idx in range(25):
    for c_idx in range(25):
        cnt = check_neighbor(r_idx, c_idx, matrix)
        if matrix[r_idx][c_idx] == 1 and (cnt == 2 or cnt ==3):
            new_generation[r_idx][c_idx] = 1
        elif matrix[r_idx][c_idx] == 1 and (cnt >= 4 or cnt <= 1):
            new_generation[r_idx][c_idx] = 0
        elif matrix[r_idx][c_idx] == 0 and (cnt == 3):
            new_generation[r_idx][c_idx] = 1
    
for row in new_generation:
    print(*row)
'''