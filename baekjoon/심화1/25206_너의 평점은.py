'''
https://www.acmicpc.net/problem/25206
너의 평점은

12:26 ~ 12:49

input
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P

output
3.284483
'''
# sol1. change_grade 함수 O
def change_grade(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0

pairs = []
total_credit = 0
for _ in range(20):
    kind, credit, grade = input().split() 

    if grade == 'P':
        continue
    grade = change_grade(grade)
    pairs.append((float(credit), float(grade)))
    total_credit += float(credit)

import math
total_sum_val = sum(math.prod(row) for row in pairs)
print(total_sum_val/total_credit)


# sol2. change_grade 함수 X
GRADE_TABLE = {'A+':4.5, 'A0':4, 'B+':3.5, 'B0':3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1,'F': 0}

prod = []
total_credit = 0
for _ in range(20):
    kind, credit, grade = input().split() 

    if grade == 'P':
        continue
    c = float(credit)
    g = float(GRADE_TABLE[grade])
    prod.append(c*g)
    total_credit += c

print(sum(prod)/total_credit)



# chage_grade 함수에 대한 여러가지 변형 방법
# sol1. 효율적이나 코드가 긺 - 시간 복잡도 면에선 효율적, 코드 길이면에선 비효율적
def change_grade(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0

# sol2. 다소 비효율적 - 이유: 인덱싱 시간복잡도 O(n)
def change_grade(grade):
    grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
    scores = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

    idx = grades.index(grade)
    return scores[idx]

# sol3. 가장 비효율적 - 이유: dictionary를 함수 호출할 때마다 호출
def change_grade(grade):
    grade_to_score = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
    }

    return grade_to_score[grade]

# sol4. 가장 효율적 - 이유: dictionary 1번 호출
GRADE_TABLE = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
    }

def change_grade(grade):
    return GRADE_TABLE[grade]