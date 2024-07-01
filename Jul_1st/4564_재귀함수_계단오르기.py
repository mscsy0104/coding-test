import sys
n = int(input())
grades = [int(sys.stdin.readline().strip()) for _ in range(n)]



def solution(n, grades):
    li = []
    for i in range(n):
        if i + 1 <= n:
            if grades[i] < grades[i+1]:
                li.append(grades[i+1])
            else:
                li.append(grades[i])
        else:
            pass
    return




