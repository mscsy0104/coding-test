'''
14:50 ~ 15:00
https://school.programmers.co.kr/learn/courses/30/lessons/42748

input:
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

output: 
[5,6,3]
'''
def solution(array, commands):
    answer = []
    
    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[-1] - 1
        sub = sorted(array[i:j])
        n = sub[k]
        answer.append(n)

    return answer