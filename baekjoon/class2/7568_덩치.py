'''
https://www.acmicpc.net/problem/7568
14:22 ~ 15:00(X)

input
5
55 185
58 183
88 186
60 175
46 155

output
2 2 1 2 5
'''

# sol. 맞는 풀이
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

grades = []
for i in range(n):
    rank = 1  # 기본 등수는 1위로 시작
    for j in range(n):
        if i == j:
            continue
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rank += 1  # 나보다 덩치 큰 사람 수 만큼 등수 밀려남
    print(rank, end = ' ')


# 맞는 풀이 일부 - 리스트 컴프리헨션 적용
grades = [
    1 + sum(1 for j in range(n) if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1])
    for i in range(n)
]

print(*grades)

# 틀린 풀이 일부
grades = []

for i in range(len(arr)):
    grade = 0
    for j in range(len(arr)):
        xi, yi = arr[i]
        xj, yj = arr[j]

        if xi == xj and yi == yj:
            continue
        elif xi > xj and yi > yj:
            grade += 1

    grades.append(grade)

li = [len(arr) - grades[i] for i in range(len(grades))]
print(li)



'''
맞는 풀이(A) v.s. 틀린 풀이(B) 
원인: 전제 차이

A 기준: 나보다 얼마나 더 큰 사람이 있는가?
B 기준: 내가 몇 명보다 큰가? (전체에서 빼면 내 순위이려나?)
'''