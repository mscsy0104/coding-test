'''
https://www.acmicpc.net/problem/10798
세로읽기

input

ABCDE
abcde
01234
FGHIJ
fghij

output
Aa0FfBb1GgCc2HhDd3IiEe4Jj
'''

# sol1. 
board = [list(input()) for _ in range(5)]

idx = 0 
len_li = [len(i) for i in board]
len_max = max(len_li)
for i in board:
    if len(i) < len_max:
        remain_count = len_max - len(i)
        i.extend(['' for _ in range(remain_count)])

result = ''
while idx < len_max:
    for i in range(5):
        result += board[i][idx]

    idx += 1

print(result)

# sol2. sol1보다 효율적인 코드
'''
sol1에서 배효율 적인 부분
1. 인덱스 길이 안 맞는 부분 패딩 처리('')
2. 문자열(스트링) 그대로 써도 되는데 2차원 리스트로 바꾼 부분
(분류가 2차원 배열이라 그렇게 풀었던 것이긴 함.)

sol1과 sol2에서의 차이점
'최대 15까지'라는 요구사항 인식
'''
board = [input() for _ in range(5)]

result = ''

for col in range(15): # 최대 15자리까지
    for row in range(5):
        if col < len(board[row]):
            result += board[row][col]

print(result)