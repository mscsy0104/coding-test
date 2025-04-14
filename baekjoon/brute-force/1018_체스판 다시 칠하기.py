'''
https://www.acmicpc.net/problem/1018
체스판 다시 칠하기

18:37 ~ ///(1시간 50분)

input
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

output
12
'''



'''
1. 8*8 가능한 잘라내는 수 구하기
2. 함수: 8*8 가정하고, WB패턴인지 BW패턴인지 확인하는 게 필요
3. 경우의 수 모아서 제일 작은 값
'''

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

row_li = [(i, i + 7) for i in range(len(board) - 7)]
col_li = [(i, i + 7) for i in range(len(board[0]) - 7)]

cnt = 0
board_li = []

for i in row_li:
    for j in col_li:
        board_unit = []
        for row in board[i[0]:i[1] + 1]:
            board_unit.append(row[j[0]: j[1] + 1])
        board_li.append(board_unit)

def count_boards_to_fix(board, first):
    cnt = 0

    if first == 'W':
        target = 'W'
        nontarget = 'B'
    else:
        target = 'B'
        nontarget = 'W'

    for r_idx, row in enumerate(board):
        for c_idx, val in enumerate(row):
            if r_idx % 2 == 0 and c_idx % 2 == 0:
                if val != target:
                    cnt += 1
                    continue
            if r_idx % 2 == 0 and c_idx % 2 != 0:
                if val != nontarget:
                    cnt += 1
                    continue
            if r_idx % 2 != 0 and c_idx % 2 == 0:
                if val != nontarget:
                    cnt += 1
                    continue
            if r_idx % 2 != 0 and c_idx % 2 != 0:
                if val != target:
                    cnt += 1
                    continue
    return cnt

cnt_li = []
for board in board_li:
    cnt_li.append(count_boards_to_fix(board, 'W'))
    cnt_li.append(count_boards_to_fix(board, 'B'))

print(min(cnt_li))