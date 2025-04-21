'''
https://www.acmicpc.net/problem/2754
학점계산

input
A0

output
4.0
'''

# sol1. hashmap 이용
hashmap = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7, 
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
    }

print(hashmap[input()])


# sol2. ASCII 기반 로직 - 더 효율적
grade = input()
credit = 69 - ord(grade[0])
if len(grade) == 2:
    if grade[1] == '+':
        credit += 0.3
    elif grade[1] == '-':
        credit -= 0.3
elif len(grade) == 1:
    credit = 0

print(float(credit))

'''
sol1, sol2 모두 좋은 방식이다.
가독성과 명확성 중요, 구조 복잡한 경우 -> sol1
코드가 짧고 규칙적인 등급 구조일 때 -> sol2
'''