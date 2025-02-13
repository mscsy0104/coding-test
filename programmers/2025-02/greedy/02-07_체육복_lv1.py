'''16:00 ~ 18:00/retry 
https://school.programmers.co.kr/learn/courses/30/lessons/42862
input:
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

output:
5
'''
def solution(n, lost, reserve):
    answer = 0
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    answer = n - len(lost_set)

    return answer