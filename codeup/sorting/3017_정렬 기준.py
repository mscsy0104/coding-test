'''
https://codeup.kr/problem.php?id=3017
3017 : 정렬 기준

18:10 ~ 다음날 다시(해설)
알게된 점
1. namedtuple, struct 사용법
2. 버블정렬(이중 for문)의 2가지 작성법
2-1) for i in range(n) for j in range(n - i - 1):
2-2) for i in range(1, n) for j in range(n-1):
n = 5일 때, 
2-1) 바깥 반복문 횟수: 5, 안 반복문 횟수: 4
2-2) 바깥 반복문 횟수: 4, 안 반복문 횟수: 4
2-1, 2-2는 같은 용도(실제 비교횟수가 중요함.)

input
5
100 90
90 100
80 80
80 90
60 50

output
1 100 90
2 90 100
4 80 90
3 80 80
5 60 50
'''

# sol1: collectoins.namedtuple
import sys
from collections import namedtuple

student = namedtuple('student', ['id', 'math', 'comp'])
students = list()

n = int(sys.stdin.readline())
for i in range(n):
    m, c = map(int, sys.stdin.readline().split())
    students.append(student(i, m, c))

def swap_loc(idx):
    students[idx], students[idx+1] = students[idx+1], students[idx]

for i in range(1, n):
    for j in range(n - i):
        if students[j].math < students[j+1].math:
            swap_loc(j)

        elif students[j].math == students[j+1].math:
            if students[j].comp < students[j+1].comp:
                swap_loc(j)

for i in range(n):
    print(students[i].id + 1, students[i].math, students[i].comp)


# sol2: struct
import sys, struct

n = int(sys.stdin.readline())
structs = list()

for i in range(n):
    m, c = map(int, sys.stdin.readline().split())
    structs.append(struct.pack('iii', i + 1, m, c))

def swap_loc(idx):
	structs[idx], structs[idx+1] = structs[idx+1], structs[idx]
	
for i in range(1, n):
	for j in range(n - i):
		st1 = struct.unpack('iii', structs[j])
		st2 = struct.unpack('iii', structs[j+1])
		if st1[1] < st2[1]:
			swap_loc(j)
		elif st1[1] == st2[1]:
			if st1[2] < st2[2]:
				swap_loc(j)


for i in structs:
	target = struct.unpack('iii', i)
	print(target[0], target[1], target[2])
		 


# 복기 + @ 
'''
1. 입력: 여러가지 데이터(= 리스트, 튜플, 네임드튜플, 스트럭트)
2. 알고리즘: 정렬, (점수: 수학 > 정보, 번호 빠름)
3. 자료구조: 네임드튜플, 튜플, 스트럭트
4. 시간복잡도: On^2까지는 가능 => 요소 비교(이중 for문)
'''
import collections

n = int(input())
student = collections.namedtuple('student', ['id', 'math', 'comp'])
# 출력 요구사항에 맞게 자료구조 구성
# <class '__main__.student'>

students = []
for i in range(n):
	m, c = map(int, input().split())
	students.append(student(i, m, c))
# [student(id=0, math=100, comp=90), student(id=1, math=90, comp=100), student(id=2, math=80, comp=80), student(id=3, math=80, comp=90), student(id=4, math=60, comp=50)]
# TOL


def swap_loc(idx):
	students[idx], students[idx+1] = students[idx+1], students[idx]
    # 다른 방식(C-style)   
    # temp = students[idx]
    # students[idx] = students[idx+1]
    # students[idx+1] = temp
	
for i in range(1, n): 
	for j in range(n - i):
		if students[j].math < students[j+1].math:
			swap_loc(j)
		elif students[j].math == students[j+1].math:
			if students[j].comp < students[j+1].comp:
				swap_loc(j)
				
for i in range(n):
	target = students[i]
	print(target.id + 1, target.math, target.comp)
	

