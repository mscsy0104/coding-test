'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576

input
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

output
"mislav"
'''
from collections import Counter

def solution(participant, completion):
    answer = ''
    hashmap = Counter(participant)
    for c in completion:
        if c in hashmap.keys():
            hashmap[c] -= 1
    for k, v in hashmap.items():
        if v != 0:
            answer = k
    return answer